import pandas as pd

# Load CSV
df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

# Convert to numeric
for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Check missing values after conversion
print(
    "Missing Return Values:"
)
print(
    df[return_cols].isnull().sum()
)

# Expense ratio validation
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print(
    "Invalid Expense Ratios:",
    len(invalid_expense)
)

# Return anomalies
anomalies = df[
    (df["return_1yr_pct"] > 100)
    |
    (df["return_1yr_pct"] < -50)
]

print(
    "Anomaly Rows:",
    len(anomalies)
)

# Save cleaned file
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("File Saved Successfully")