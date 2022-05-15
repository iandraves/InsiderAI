import h2o
import pandas as pd
from insidertrading.data import raw_data
from insidertrading.data import invalid_entries
from insidertrading.data import binary_transform
from insidertrading.data import unused_entries
from insidertrading.predictor import model
h2o.init()

FH_API_KEY = 'c9gvf4qad3iblo2fou70'

START_DATE = '2021-01-01'
END_DATE = '2022-01-01'


def main():
    ''' RETRIEVE RAW DATA FROM S&P 500 '''
    print("\nDOWNLOADING S&P 500 DATA...")
    data = raw_data.retrieve(START_DATE, END_DATE, FH_API_KEY)
    data.to_csv("data/raw_data.csv", index=False)

    ''' CLEAN & SAVE DATA '''
    print("\nCLEANING DATA...")

    # Remove duplicates
    print("---> Removing duplicates")
    data.drop_duplicates()

    # Remove invalid entries
    print("---> Removing invalid entries")
    data = invalid_entries.find_and_drop(data)

    # Apply binary transformation to future prices (0 = down, 1 = up)
    print("---> Applying binary transformation")
    data = binary_transform.apply(data)

    # Remove unused entries
    print("---> Removing unused entries")
    data = unused_entries.drop(data)

    # Save cleaned data
    print("---> Saving cleaned data")
    data.to_csv("data/final_data.csv", index=False)

    ''' CREATE AND TRAIN MODEL & GET PREDICTIONS '''
    print("\nGENERATING MODEL AND GETTING PREDICTIONS...")
    # Import dataset to h2o
    data = h2o.import_file("data/final_data.csv")

    # Get 1 day, 7 day, 14 day, and 30 day predictions
    print("---> Predicting 1 day out")
    one_day_predictions = model.create_train_predict(data, "oneDay")

    print("---> Predicting 1 week out")
    seven_day_predictions = model.create_train_predict(data, "sevenDay")

    print("---> Predicting 2 weeks out")
    fourteen_day_predictions = model.create_train_predict(data, "fourteenDay")

    print("---> Predicting 1 month out")
    thirty_day_predictions = model.create_train_predict(data, "thirtyDay")

    # Save predictions
    print("---> Saving predictions")
    one_day_predictions.to_csv(
        "predictions/one_day_predictions.csv", index=False)
    seven_day_predictions.to_csv(
        "predictions/seven_day_predictions.csv", index=False)
    fourteen_day_predictions.to_csv(
        "predictions/fourteen_day_predictions.csv", index=False)
    thirty_day_predictions.to_csv(
        "predictions/thirty_day_predictions.csv", index=False)


if __name__ == "__main__":
    main()
