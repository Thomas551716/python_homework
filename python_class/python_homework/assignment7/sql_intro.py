import sqlite3

# Task 1: Create and connect to the database
def create_connection():
    try:
        conn = sqlite3.connect("../db/magazines.db")
        conn.execute("PRAGMA foreign_keys = 1")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    
# Task 2: Create tables
def create_tables(conn):
    try:
        cur = conn.cursor()
        cur.excute("""
            CREATE TABLE IF NOT EXIST publishers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS magazines(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCE publishers(id)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                UNIQUE(name, address)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY(subscriber_id) REFERENCES subscribers(id),
                FOREIGN KEY(magazine_id) REGERENCES magazines(id),
            );
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
    
# Task 3: Add data
def insert_publisher(conn, name):
    try:
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO publishers (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting publisher: {e}")

def insert_magazine(conn, name, publisher_id):
    try:
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting magazine: {e}")

def insert_subscriber(conn, name, address):
    try:
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting subscriber: {e}")

def insert_subscription(conn, subscriber_id, magazine_id, expiration_date):
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT OR IGNORE INTO subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
        """, (subscriber_id, magazine_id, expiration_date))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting subscription: {e}")

# Task 4: Queries
def run_queries(conn):
    try:
        cur = conn.cursor()
        print("\nAll subscribers:")
        for row in cur.execute("SELECT * FROM subscribers"):
            print(row)
        print("\nMagazines sorted by name:")
        for row in cur.execute("SELECT * FROM magazines ORDER BY name"):
            print(row)
        print("\nMagazines for a specific publisher (id = 1):")
        for row in cur.execute("""
            SELECT magazines.name FROM magazines
            JOIN publishers ON magazines.publisher_id = publishers.id
            WHERE publishers.id = 1
        """):
            print(row)
    except sqlite3.Error as e:
        print(f"Error querying database: {e}")
# Main execution
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        create_tables(conn)
        insert_publisher(conn, "CTD Publishing")
        insert_publisher(conn, "TechWorld Media")
        insert_publisher(conn, "Green Planet Weekly")
        insert_magazine(conn, "Python Weekly", 1)
        insert_magazine(conn, "Tech Today", 2)
        insert_magazine(conn, "Eco Life", 3)
        insert_subscriber(conn, "Alice Smith", "123 Maple St")
        insert_subscriber(conn, "Bob Jones", "456 Oak Ave")
        insert_subscriber(conn, "Carol White", "789 Pine Rd")
        insert_subscription(conn, 1, 1, "2025-12-31")
        insert_subscription(conn, 2, 2, "2025-11-30")
        insert_subscription(conn, 3, 3, "2025-10-15")
        run_queries(conn)
        conn.close()