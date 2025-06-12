import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
conn = sqlite3.connect("sales_data.db")

query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""
df = pd.read_sql_query(query, conn)
conn.close()
print("Sales Summary:")
print(df)

plt.figure(figsize=(8, 6))
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.grid(axis='y')
plt.tight_layout()

# Save and show chart
plt.savefig("sales_chart.png")
plt.show()
