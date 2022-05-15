def apply(df):
    for i in range(len(df)):
        zero_day_price = float(df['zeroDay'].iat[i])
        one_day_price = float(df['oneDay'].iat[i])
        seven_day_price = float(df['sevenDay'].iat[i])
        fourteen_day_price = float(df['fourteenDay'].iat[i])
        thirty_day_price = float(df['thirtyDay'].iat[i])

        # 1 day
        if one_day_price - zero_day_price > 0:
            df['oneDay'].iat[i] = 1
        else:
            df['oneDay'].iat[i] = 0

        # 7 day
        if seven_day_price - zero_day_price > 0:
            df['sevenDay'].iat[i] = 1
        else:
            df['sevenDay'].iat[i] = 0

        # 14 day
        if fourteen_day_price - zero_day_price > 0:
            df['fourteenDay'].iat[i] = 1
        else:
            df['fourteenDay'].iat[i] = 0

        # 30 day
        if thirty_day_price - zero_day_price > 0:
            df['thirtyDay'].iat[i] = 1
        else:
            df['thirtyDay'].iat[i] = 0

    return df
