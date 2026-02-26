import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Order Date": [
        "2024-01-10", "2024-02-15", "2024-03-20",
        "2024-04-12", "2024-05-18", "2024-06-25"
    ],
    "Product Name": [
        "Chair", "Table", "Laptop", "Chair", "Phone", "Laptop"
    ],
    "Sales": [200, 450, 1200, 300, 800, 1500]
})


df["Order Date"] = pd.to_datetime(df["Order Date"])

print("Dataset loaded successfully\n")
#clean
df.dropna(inplace=True)

#total revenue
total_revenue = df["Sales"].sum()
print("Total Revenue:", total_revenue)

# top products
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Products:")
print(top_products)

# monthly sales trend
df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.month)["Sales"]
    .sum()
)

# plot graph
plt.figure()
monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()