def find_and_drop(df):
    for i in range(len(df)):
        dollar_amount = int(df['dollarAmount'][i])
        trade_type = df['buyOrSale'][i]
        future_price = df['zeroDay'][i]
        portfolio_change = str(df['insiderPortfolioChange'][i])

        if dollar_amount == 0 or trade_type == "Gift" or future_price == "" or any(c.isalpha() for c in portfolio_change):
            df = df.drop(labels=None, axis=0, index=i, columns=None,
                         level=None, inplace=False, errors='raise')

    return df
