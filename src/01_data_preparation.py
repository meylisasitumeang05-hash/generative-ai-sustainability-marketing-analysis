import pandas as pd

# Load data
df = pd.read_excel("Data Penelitian.xlsx")

# Cleaning
df.columns = df.columns.str.strip()
df['X_AGM'] = df['X_AGM'].astype(str).str.strip()
df['W_PAS'] = df['W_PAS'].astype(str).str.strip()

# Encode treatment
df["Treatment"] = df["X_AGM"] + "_" + df["W_PAS"]

print(df.head())
