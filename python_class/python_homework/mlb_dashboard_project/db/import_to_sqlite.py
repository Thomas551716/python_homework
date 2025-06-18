import pandas as pd
import sqlite3
import os

# Path to your CSVs
csv_folder = "../scraping/"
csv_files = ["mlb_events.csv"]  # Add more if you have them

# Create database connection
conn = sqlite3.connect("mlb_data.db")
cursor = conn.cursor()
for file_name in csv_files:
    table_name = os.path.splitext(file_name)[0]  # e.g., "mlb_events"
    file_path = os.path.join(csv_folder, file_name)
    print(f"Importing {file_path} into table '{table_name}'...")

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        continue

    # Load CSV into DataFrame
    df = pd.read_csv(file_path)

    # Import into SQLite table
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"✅ Imported {len(df)} rows into '{table_name}'.")
   

conn.commit()
conn.close()
print("🎉 All CSV files imported into mlb_data.db.")