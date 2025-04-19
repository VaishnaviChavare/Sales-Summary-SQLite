#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# In[9]:


# Load SQLite database
conn = sqlite3.connect("sales_data.db")

# Create and insert data — only needed once
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")
sample_data = [
    ("Apple", 10, 1.2),
    ("Banana", 5, 0.5),
    ("Orange", 8, 0.8),
    ("Apple", 15, 1.2),
    ("Banana", 20, 0.5)
]
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()


# In[10]:


# Run basic SQL
query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""


# In[11]:


# Load into pandas
df = pd.read_sql_query(query, conn)
df


# In[12]:


# Plot simple bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue ($)")
plt.tight_layout()


# In[13]:


# Save chart
plt.savefig("sales_chart.png")
plt.show()


# In[7]:


# Step 6: Plotting bar charts
plt.figure(figsize=(8, 5))
plt.bar(df["product"], df["total_quantity"], label="Total Quantity", alpha=0.7)
plt.bar(df["product"], df["total_revenue"], label="Total Revenue ($)", alpha=0.7)
plt.title("Sales Summary")
plt.xlabel("Product")
plt.ylabel("Quantity / Revenue")
plt.legend()
plt.tight_layout()
plt.show()


# In[14]:


# Close connection
conn.close()


# In[ ]:




