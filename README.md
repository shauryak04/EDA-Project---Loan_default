# Loan Default – Exploratory Data Analysis

Explore borrower characteristics to see which factors are associated with loan default.

## Dataset

**File:** `data/loan_default.csv`

Key columns used:

- Default – whether the borrower defaulted
- Income
- CreditScore
- LoanAmount

## What the analysis does

1. Inspect structure and summary statistics
2. Check for missing values and duplicate rows
3. Measure the default rate
4. Compare income, credit score and loan amount for defaulters vs non-defaulters
5. Engineer a `LoanToIncome` ratio (`LoanAmount / Income`) and compare it across groups
6. Correlation of numeric features

## Visualisations

| Chart | Type |
|-------|------|
| Default vs Non-default Count | Bar chart |
| Income vs Default | Box plot |
| Credit Score vs Default | Box plot |
| Loan Amount vs Default | Box plot |
| Loan-to-Income vs Default | Box plot |
| Correlation Heatmap | Heatmap of numeric features |

## Questions explored

- Do defaulters have lower income or credit scores?
- Is a high loan-to-income ratio a warning sign for default?
- Which numeric features are most correlated with default?

## Key insights

<!-- Run the script and write 3–5 findings here, e.g. "Customers in X had the highest ..." -->

- _Add your findings here_

## How to run

From the root of the repository:

```bash
pip install -r requirements.txt
python 08_loan_default_eda/loan_default_eda.py
```

Make sure `loan_default.csv` is in the `data/` folder. Each chart opens in a window; close it to see the next one.

## Tools

Python · pandas · matplotlib · seaborn

---
[← Back to all projects](../README.md)
