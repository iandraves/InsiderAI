import pandas as pd
import numpy as np
import finnhub
import yfinance as yf
import pandas_market_calendars as mcal
import time


def retrieve(start, end, FH_API_KEY):
    NYSE_CALENDAR = mcal.get_calendar('NYSE').valid_days(
        start_date=start, end_date=end)

    # Get S&P 500 stocks
    table = pd.read_html(
        'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    sp500 = table[0]['Symbol']

    # Get data from each stock
    dfs = []
    fhc = finnhub.Client(api_key=FH_API_KEY)
    for stock in sp500:
        insider_trades = fhc.stock_insider_transactions(
            stock, start, end)

        # Convert the data into a dataframe.
        df = pd.DataFrame(data=insider_trades['data'])

        if not df.empty:
            # Getting price data
            price_dict = {}
            prices = yf.download(stock, start=start,
                                 end=end)['Close']
            dates = []
            if len(prices) == len(NYSE_CALENDAR):
                for i in range(len(NYSE_CALENDAR)):
                    date = NYSE_CALENDAR[i].date().strftime('%Y-%m-%d')
                    dates.append(date)
                    price = prices[i]
                    price_dict.update({date: price})

                # Derived attributes from the data.
                df['dollarAmount'] = df['change'] * df['transactionPrice']
                df['insiderPortfolioChange'] = df['change'] / \
                    (df['share'] - df['change'])

                conditions = [
                    (df['change'] >= 0) & (df['transactionPrice'] > 0),
                    (df['change'] <= 0) & (df['transactionPrice'] > 0),
                    (df['transactionPrice'] == 0)
                ]
                values = ['Buy', 'Sale', 'Gift']
                df['buyOrSale'] = np.select(conditions, values)

                zero_day_prices = []
                one_day_prices = []
                seven_day_prices = []
                fourteen_day_prices = []
                thirty_day_prices = []

                for date in df['transactionDate']:
                    zero, one, seven, fourteen, thirty = "", "", "", "", ""

                    try:
                        if (dates.index(date) + 30) < len(dates):
                            zero = price_dict.get(date)
                            one = price_dict.get(
                                dates[dates.index(date) + 1])
                            seven = price_dict.get(
                                dates[dates.index(date) + 7])
                            fourteen = price_dict.get(
                                dates[dates.index(date) + 14])
                            thirty = price_dict.get(
                                dates[dates.index(date) + 30])
                    except ValueError:
                        pass

                    zero_day_prices.append(zero)
                    one_day_prices.append(one)
                    seven_day_prices.append(seven)
                    fourteen_day_prices.append(fourteen)
                    thirty_day_prices.append(thirty)

                df['zeroDay'] = zero_day_prices
                df['oneDay'] = one_day_prices
                df['sevenDay'] = seven_day_prices
                df['fourteenDay'] = fourteen_day_prices
                df['thirtyDay'] = thirty_day_prices

                dfs.append(df)

                time.sleep(1)  # Prevents overloading API

    return pd.concat(dfs, axis=0, ignore_index=True)
