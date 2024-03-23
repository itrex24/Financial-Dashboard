import pandas as pd
import os
import shutil


def clean_monzo_data(file_path):
    # Load the CSV data
    df = pd.read_csv(file_path)
    
    # Drop unnecessary columns
    columns_to_drop = [
        'Transaction ID', 'Time', 'Emoji', 'Currency', 
        'Local amount', 'Local currency', 'Notes and #tags', 
        'Address', 'Receipt', 'Description', 'Category split', 
        'Money Out', 'Money In'
    ]
    df.drop(columns_to_drop, axis=1, inplace=True)
    
    # Rename columns
    df.rename(columns={
        'Type': 'Subcategory',
        'Name': 'Entity'
    }, inplace=True)
    
    # Convert date column to datetime format and reformat it
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y').dt.strftime('%d/%m/%Y')
    
    # Reorder columns
    df = df[['Date', 'Amount', 'Subcategory', 'Entity', 'Category']]
    
    return df


def process_files(raw_data_dir, clean_data_dir, monzo_identifier='Monzo'):
    # Ensure the clean data directory exists
    os.makedirs(clean_data_dir, exist_ok=True)
    
    # Ensure the 'finished' subdirectory exists
    finished_dir = os.path.join(raw_data_dir, 'finished')
    os.makedirs(finished_dir, exist_ok=True)
    
    # Iterate through each file in the raw data directory
    for file_name in os.listdir(raw_data_dir):
        if file_name.endswith('.csv') and monzo_identifier in file_name:
            print(f"Processing {file_name}...")
            file_path = os.path.join(raw_data_dir, file_name)
            
            # Clean the data
            cleaned_df = clean_monzo_data(file_path)
            
            # Construct new file name and path
            new_file_name = f"(new){file_name}"
            new_file_path = os.path.join(clean_data_dir, new_file_name)
            
            # Save the cleaned data to the new file
            cleaned_df.to_csv(new_file_path, index=False)
            print(f"Cleaned data saved to {new_file_name}")
            
            # Move the original file to the 'finished' directory
            shutil.move(file_path, os.path.join(finished_dir, file_name))
            print(f"Moved processed file to {os.path.join(finished_dir, file_name)}")

if __name__ == "__main__":
    raw_data_dir = 'data/raw data'
    clean_data_dir = 'data/clean data'
    process_files(raw_data_dir, clean_data_dir)
    print("Data cleaning processed completed successfully")