import h2o
from h2o.estimators.gbm import H2OGradientBoostingEstimator
h2o.init()


def create_train_predict(data, timeframe):
    # Convert the future price column to a factor
    data[timeframe] = data[timeframe].asfactor()

    # Split the data into train and test
    train, test = data.split_frame(ratios=[.75], seed=1234)

    # Generate a GBM model using the training dataset
    model = H2OGradientBoostingEstimator(distribution="bernoulli",
                                         ntrees=100,
                                         max_depth=4,
                                         learn_rate=0.1,
                                         seed=1234)
    model.train(y=timeframe,
                x=["share", "change", "dollarAmount", "insiderPortfolioChange"],
                training_frame=train)

    # Predict using the GBM model and the testing dataset
    prediction = model.predict(test)

    return prediction.as_data_frame()
