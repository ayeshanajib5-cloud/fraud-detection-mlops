import os
import pandas as pd

DATA_PATH = "data/creditcard.csv"

def check_data_available():
    if not os.path.exists(DATA_PATH):
        print("Dataset not found. Drift check skipped.")
        return False
    return True

def detect_drift():
    if not check_data_available():
        return

    df = pd.read_csv(DATA_PATH)

    missing_values = df.isnull().sum().sum()
    total_rows = len(df)

    print("Drift Detection Report")
    print("----------------------")
    print(f"Total rows checked: {total_rows}")
    print(f"Missing values found: {missing_values}")

    if missing_values > 0:
        print("Potential data quality issue detected.")
    else:
        print("No major data quality drift detected.")

if __name__ == "__main__":
    detect_drift()