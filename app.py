import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("loan_default.csv")
print(df.head())
print(df.info())

df["Default"].value_counts.plot(kind="bar")
plt.title("Default vs non-default count")
plt.show()

sns.boxplot(data=df,x="Default",y="Income")
plt.title("income vs default")
plt.show()

sns.boxplot(data=df,x="Default",y="CreditScore")
plt.title("Credit score vs default")
plt.show()

sns.boxplot(data=df,x="Default",y="LoanAmount")
plt.title("Loan amount vs default")
plt.show()

loan["LoanToIncome"] = loan["LoanAmount"] / loan["Income"]
sns.boxplot(data=loan, x="Default", y="LoanToIncome")
plt.title("Loan-to-Income vs Default")
plt.show()

num_cols = loan.select_dtypes(include=["int64", "float64"])
sns.heatmap(num_cols.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap - Loan Data")
plt.show()
