import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#connect to the database using relative path
conn = sqlite3.connect('../db/lesson.db')

# Run your query with pandas
query = """
SELECT last_name, SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""
# Load query results into a DataFrame
employee_results = pd.read_sql_query(query, conn)
conn.close()

# Plotting
employee_results.plot(kind='bar', x='last_name', y='revenue', color='orange', legend=False)
plt.title('Revenue by Employee')
plt.xlabel('Employee Last Name')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.show()