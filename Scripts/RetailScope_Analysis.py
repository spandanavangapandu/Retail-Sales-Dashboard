# RetailScope: Visualizing Sales Performance

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv('Superstore.csv', encoding='latin1')

# Step 2: Basic cleanup
df.drop_duplicates(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month_name()

# Step 3: Generate KPIs
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100
best_category = df.groupby('Category')['Profit'].sum().idxmax()

# Print KPIs
print("📊 Total Sales: ₹{:,.2f}".format(total_sales))
print("💰 Total Profit: ₹{:,.2f}".format(total_profit))
print("📈 Profit Margin: {:.2f}%".format(profit_margin))
print("🏆 Best Category by Profit:", best_category)

# Step 4: Grouped summaries
sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
profit_by_segment = df.groupby('Segment')['Profit'].sum().sort_values(ascending=False)

print("\nSales by Region:\n", sales_by_region)
print("\nProfit by Segment:\n", profit_by_segment)

# Step 5: Export cleaned data
df.to_csv('Cleaned_Superstore.csv', index=False)
print("\n✅ Cleaned data saved as 'Cleaned_Superstore.csv'")

# Step 6: Monthly Sales Trend Plot
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']
monthly_sales['Month'] = pd.Categorical(monthly_sales['Month'], categories=month_order, ordered=True)
monthly_sales.sort_values(by=['Year', 'Month'], inplace=True)

plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Sales', hue='Year', marker='o')
plt.title('📆 Monthly Sales Trend')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Monthly_Sales_Trend.png')  # Saves plot as image
plt.show()

print("✅ Sales trend plot saved as 'Monthly_Sales_Trend.png'")
