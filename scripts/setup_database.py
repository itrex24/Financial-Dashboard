import sqlite3
import os

# Define the path to the database
database_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'finance_dashboard.db')

# Connect to the SQLite database (it will be created if it doesn't exist in the 'data' directory)
conn = sqlite3.connect(database_path)

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Define the SQL statement for creating the transactions table
create_table_query = '''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        account TEXT NOT NULL,
                        date TEXT NOT NULL,
                        amount REAL NOT NULL,
                        payment_category TEXT NOT NULL,
                        entity TEXT NOT NULL
                    );'''

# Execute the SQL statement to create the table
cursor.execute(create_table_query)

# Commit the changes and close the connection to the database
conn.commit()
conn.close()

print("Database setup completed successfully.")
