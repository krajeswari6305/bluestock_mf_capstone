import pandas as pd

perf = pd.read_csv(
    r"C:\bluestock_mf_capstone\data\processed\scheme_performance_clean.csv"
)

risk = input(
    "Enter Risk Appetite: "
)

result = (
    perf[
        perf["risk_grade"].str.lower()
        == risk.lower()
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds\n")

print(
    result[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]
)