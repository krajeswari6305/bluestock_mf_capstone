-- 1. Top 5 Funds by AUM

SELECT
scheme_name,
aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV Per Month

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;


-- 3. Transactions by State

SELECT
state,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 4. Funds with Expense Ratio < 1%

SELECT
scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;


-- 5. Transaction Amount by Type

SELECT
transaction_type,
SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY transaction_type;


-- 6. Average 3-Year Return by Fund House

SELECT
fund_house,
AVG(return_3yr_pct) AS avg_return
FROM scheme_performance
GROUP BY fund_house
ORDER BY avg_return DESC;


-- 7. Average 1-Year Return by Category

SELECT
category,
AVG(return_1yr_pct) AS avg_return
FROM scheme_performance
GROUP BY category
ORDER BY avg_return DESC;


-- 8. Risk Grade Distribution

SELECT
risk_grade,
COUNT(*) AS total_funds
FROM scheme_performance
GROUP BY risk_grade;


-- 9. Transactions by Payment Mode

SELECT
payment_mode,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY payment_mode
ORDER BY total_transactions DESC;


-- 10. Top Cities by Investment Amount

SELECT
city,
SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY city
ORDER BY total_amount DESC
LIMIT 10;