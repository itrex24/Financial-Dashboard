import pandas as pd
import os

def clean_csv(file_path):
    # Load the CSV data
    df = pd.read_csv(file_path)
    
    # Example cleaning steps:
    # Rename columns for consistency
    df.rename(columns={
        'Date': 'date',
        'Amount': 'amount',
        'Payment Category': 'payment_category',
        'Account': 'account',
        'Entity': 'entity'
    }, inplace=True)
    
    # Convert date column to datetime format
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    
    # You can add more cleaning steps here as needed
    
    return df

def main():
    # Directory where raw CSV files are stored
    raw_data_dir = os.path.join('data', 'raw data')
    # Directory where cleaned CSV files will be saved
    clean_data_dir = os.path.join('data', 'clean data')
    
    # Ensure the clean data directory exists
    os.makedirs(clean_data_dir, exist_ok=True)
    
    # Iterate through each file in the raw data directory
    for file_name in os.listdir(raw_data_dir):
        file_path = os.path.join(raw_data_dir, file_name)
        # Clean the data
        cleaned_df = clean_csv(file_path)
        # Save the cleaned data to a new file in the clean data directory
        cleaned_file_path = os.path.join(clean_data_dir, f"cleaned_{file_name}")
        cleaned_df.to_csv(cleaned_file_path, index=False)
        print(f"Cleaned data saved to {cleaned_file_path}")

if __name__ == "__main__":
    main()
