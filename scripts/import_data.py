import os
import pandas as pd
import sqlite3


import os
import pandas as pd
import sqlite3

def import_csv_to_db(csv_file_path, db_path):
    # Read the cleaned data from CSV
    df = pd.read_csv(csv_file_path)
    
    # Check the first few rows of the DataFrame, including the Date column
    print(df.head())
    
    # Shows how many NULL or NaT values are present
    print(df['Date'].isnull().sum())

    try:
        # Using a context manager to handle the database connection
        with sqlite3.connect(db_path) as conn:
            # Write the data to a SQLite table
            df.to_sql('transactions', conn, if_exists='append', index=False)
    except Exception as e:
        print(f"Error importing {csv_file_path}: {e}")



def import_all_cleaned_files(clean_data_dir, db_path):
    # Iterate over all CSV files in the clean data directory
    for file_name in os.listdir(clean_data_dir):
        if file_name.endswith('.csv'):
            print(f"Importing {file_name} into the database...")
            csv_file_path = os.path.join(clean_data_dir, file_name)
            import_csv_to_db(csv_file_path, db_path)
            print(f"Successfully imported {file_name}.")


if __name__ == "__main__":
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # This navigates up twice from the current file's directory
    clean_data_dir = os.path.join(project_dir, 'data', 'clean data')
    db_path = os.path.join(project_dir, 'data', 'finance_dashboard.db')
    import_all_cleaned_files(clean_data_dir, db_path)
    print("imported data to database successfully")



