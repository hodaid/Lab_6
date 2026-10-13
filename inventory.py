import pandas as pd
import matplotlib.pyplot as plt

raw = {
    "Product": ["Cola", "Chips", "Milk", "Biscuits", "Juice", "Chocolate", "Yogurt", "Tea", "Coffee", "Bread"],
    "Category": ["beverages ", "SNACKS", " Dairy", "Snacks", "beverages", "snacks", "dairy ", "Beverages", "beverages", "bakery"],
    "Price": ["Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120", "Rs. 1,800", "Rs. 250", "Rs. 300", "Rs. 950", "Rs. 1,500", "Rs. 200"],
    "Stock": [40, 120, 60, 150, 80, 200, 90, 50, 45, 110]
}

df = pd.DataFrame(raw)

df["Category"] = df["Category"].str.strip().str.title()

df["Price"] = df["Price"].str.replace("Rs. ", "", regex=False).str.replace(",", "").astype(float)

df["Category_Code"] = df["Category"].astype("category").cat.codes

print("Cleaned Inventory DataFrame:")
print(df)

avg_price = df.groupby("Category")["Price"].mean()
total_stock = df.groupby("Category")["Stock"].sum()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(avg_price.index, avg_price.values, color=["#4C78A8", "#F58518", "#54A24B", "#E45756"])
axes[0].set_title("Average Price by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")
axes[0].grid(axis="y", alpha=0.3)

axes[1].pie(total_stock.values, labels=total_stock.index, autopct="%1.1f%%", startangle=90, colors=["#4C78A8", "#F58518", "#54A24B", "#E45756"])
axes[1].set_title("Stock Share by Category")

fig.suptitle("Product Inventory Overview", fontsize=16)
plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()