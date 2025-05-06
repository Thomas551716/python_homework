import sqlite3

# Task 1: Total price of each of the first 5 orders by using JOIN, GROUP BY AND Aggregation 
def task1():
    conn = sqlite3.connect("../db/lesson.db")
    conn.execute("PRAGMA foriegn_keys = 1")
    cur = conn.curson()

    query = """
    SELECT
        o.order_id,
        SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_item li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id 
    ORDER BY o.order_id
    LIMIT 5;
    """
    cur.execute(query)
    rows = cur.fetchall()
    print("Task 1: Total price for first 5 orders")
    for row in rows:
        print(f"Order ID: {row[0]}, Total Price: {row[1]:.2f}")

    conn.close()
if  __name__== "__main__":
    task1()

# Task 2: Average Order Price per Customer
def task2():
    conn = sqlite3.connect("../db/lesson.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()

    query = """
    SELECT 
        c.name,
        AVG(order_totals.total_price) AS average_total_price
    FROM customers c
    LEFT JOIN (
        SELECT
            o.customer_id AS customer_id_b,
            SUM(p.price * li.quantity) AS total_price

        FROM order o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
    ) AS order_totals ON c.customer_id = order_totals.customer_id_b
    Group BY c.customer_id;
    """
    cur.execute(query)
    rows = cur.fetchall()
    print("\nTask 2: Average order price per customer")
    for row in rows:
        print(f"Customer: {row[0]}, Average Order Price: {row[1] of row[1] else 0:.2f}")
    conn.close()

# update the botto script to call both tasks:
if __name__ == "__main__":
    task1()
    task2()

# Task 3: Insert New Order WITH A TRANSACTION
def task3():
    conn = sqlite3.connect("../db/lesson.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()

    try:
        # Start transaction
        conn.execute("BEGIN")

        # Get customer_id
        cur.execute("SELECT customer_id FROM customers WHERE name = 'Perez and Sons'")
        customer_id = cur.fetchone()[0]

        # Get employee_id 
        cur.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name ='Harris'")
        employee_id = cur.fetchone()[0]

        # Get 5 least expensive product_ids
        cur.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
        product_ids = [row[0] for row in cur.fetchall()]

        # Insert order and get order_id 
        cur.execute("""
            INSERT INTO orders (customer_id, employee_id)
            VALUES (?, ?)
            RETURNING order_id
        """, (customer_id, employee_id))
        order_id = cur.fetchone()[0]

        # Insert line_itme (10 of each product)
        for pid in product_ids:
            cur.execute("""
                INSERT INTO line_itme (order_id, product_id, quantity)
                VALUES (?, ?, ?)
            """, (order_id,pid, 10))

        #commit transaction
        conn.commit()

        # Print line_item for the new order
        cur.execute("""
            SELECT li.line_item_id, li.quantity, p.name
            FROM line_item li
            JOIN products p ON li.product_id = p.product_id
            WHERE li.order_id = ?
        """, (order_id))
        rows = cur.fetchall()
        
        print("\nTask 3: New Order Line Items")
        for row in rows:
            print(f"Line Item ID: {row[0]}, Quantity: {rows[1]}, Product: {row[2]}")
    except Exception as e:
        conn.rollback()
        print("Transaction failed:", e)
    finally :
        conn.close()

# Update main runner:
    if __name__ == "__main__":
        task1()
        task2()
        task3()
        
# Task 4: Employees with more than 5 orders
def task4():
    conn = sqlite3.connect("../db/lesson.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()

    query = """
    SELECT
        e.employee_id,
        e.first_name,
        e.last_name,
        COUNT(o.order_id) AS order_count
    FROM employees e
    JOIN orders o ON e..employee_id = o.employee_id
    GROUP By e.employee_id
    HAVING  COUNT(o.order_id) > 5;
    """
    cur.execute(query)
    rows = cur.fetchall()

    print("\nTask4: Employees with more than 5 orders")
    for row in rows:
        print(f"Employee ID: {row[0]}, Name: {row[1]} {row[2]}, Order Count: {row[3]}")
    conn.close()
# Update main runner:
    if __name__ == "__main__":
        task1()
        task2()
        task3()
        task4()
