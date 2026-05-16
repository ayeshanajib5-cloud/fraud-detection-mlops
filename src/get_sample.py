import pandas as pd

df = pd.read_csv("data/creditcard.csv")

sample = df.drop("Class", axis=1).iloc[0].tolist()

print(sample)
print("Number of features:", len(sample))