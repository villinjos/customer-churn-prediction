import pandas as pd

# Load dataset
df = pd.read_csv("data/customer_churn.csv")

# Display first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Missing values
print(df.isnull().sum())
