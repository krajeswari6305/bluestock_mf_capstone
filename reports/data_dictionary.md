# Bluestock Mutual Fund Capstone - Data Dictionary

## NAV History

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique mutual fund identifier |
| date | DATE | NAV reporting date |
| nav | FLOAT | Net Asset Value of the scheme |

---

## Investor Transactions

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | Mutual fund identifier |
| transaction_type | TEXT | SIP, Lumpsum, Redemption |
| amount_inr | INTEGER | Transaction amount in INR |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier classification |
| age_group | TEXT | Investor age category |
| gender | TEXT | Investor gender |
| annual_income_lakh | FLOAT | Annual income in lakhs |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | KYC verification status |

---

## Scheme Performance

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Mutual fund identifier |
| scheme_name | TEXT | Name of scheme |
| fund_house | TEXT | Fund house name |
| category | TEXT | Fund category |
| return_1yr_pct | FLOAT | 1-year return percentage |
| return_3yr_pct | FLOAT | 3-year return percentage |
| return_5yr_pct | FLOAT | 5-year return percentage |
| expense_ratio_pct | FLOAT | Expense ratio percentage |
| alpha | FLOAT | Alpha performance metric |
| beta | FLOAT | Beta risk metric |
| sharpe_ratio | FLOAT | Risk-adjusted return metric |
| risk_grade | TEXT | Risk classification |