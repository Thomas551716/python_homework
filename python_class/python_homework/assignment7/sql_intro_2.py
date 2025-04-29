import pandas as pd
import sqlite3

# Connect to the lesson database
conn = sqlite3.connect("../db/lesson.db")

# Read data with JOIN
query = """
    SELECT 
        line_items.line_item_id, 
        line_items.quantity, 
        line_items.product_id, 
        products.product_name, 
        products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
"""
df = pd.read_sql_query(query, conn)
print(df.head())

# Add total column
df['total'] = df['quantity'] * df['price']
print(df.head())

# Group and summarize
summary_df = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
}).rename(columns={'line_item_id': 'count'})
summary_df = summary_df.sort_values(by='product_name')
print(summary_df.head())

# Write to CSV
summary_df.to_csv("order_summary.csv")
conn.close()