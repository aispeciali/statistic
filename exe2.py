import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
    

df = pd.read_csv('data.csv')

print("First 5 rows of data:")
print(df.head())
print("\nData information:")
print(df.info())
income_columns = ['January income', 'February income', 'March income', 
                  'April income', 'May income', 'June income', 
                  'July income', 'August income', 'September income', 
                  'October income', 'November income', 'December income']


df['Average income'] = df[income_columns].mean(axis=1)

plt.figure(figsize=(10, 6))
bars = plt.bar(df['Name'], df['Average income'], color=['skyblue', 'lightgreen', 'lightcoral', 'orange', 'violet'])
plt.xlabel('Names')
plt.ylabel('Average Income')
plt.title('Monthly Average Income for Each Person (Over 12 Months)')
plt.grid(axis='y', alpha=0.3)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 20,
             f'{height:.0f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('average_income_bar.png', dpi=300)
plt.show()

plt.figure(figsize=(12, 7))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for i, person in df.iterrows():
    plt.plot(months, person[income_columns], marker='o', label=person['Name'], linewidth=2)

plt.xlabel('Months')
plt.ylabel('Income')
plt.title('Monthly Income Trend for Each Person (Over 12 Months)')
plt.legend(title='People')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('monthly_income_trend.png', dpi=300)
plt.show()

print("\nAverage income for each person:")
print(df[['Name', 'Average income']].to_string(index=False))

print("\nMonthly income data:")
income_df = df[['Name'] + income_columns]
print(income_df.to_string(index=False))