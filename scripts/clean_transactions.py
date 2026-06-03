import pandas as pd

# Load file
df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
      .str.strip()
      .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

invalid_types = df[
    ~df["transaction_type"].isin(valid_types)
]

print(
    "Invalid Transaction Types:",
    len(invalid_types)
)

# Amount validation
invalid_amounts = df[
    df["amount_inr"] <= 0
]

print(
    "Invalid Amount Rows:",
    len(invalid_amounts)
)

# KYC validation
valid_kyc = [
    "Verified",
    "Pending"
]

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print(
    "Invalid KYC Rows:",
    len(invalid_kyc)
)

# Save
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("File Saved Successfully")