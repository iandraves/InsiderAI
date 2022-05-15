def drop(df):
    df.drop(['symbol', 'name', 'filingDate', 'transactionDate',
            'transactionCode', 'transactionPrice', 'buyOrSale'], axis=1, inplace=True)

    return df
