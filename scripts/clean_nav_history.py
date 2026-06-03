import pandas as pd

# Load CSV
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort values
df = df.sort_values(["amfi_code", "date"])

# Duplicate check
print("Duplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Missing NAV check
print("Missing NAV:", df["nav"].isnull().sum())

# Forward fill NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Validate NAV > 0
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV rows:", len(invalid_nav))

# Save cleaned file
df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("File Saved Successfully")