import pandas as pd
import os
import shutil

def clean_barclays_data(file_path):
    # Load the CSV data
    df = pd.read_csv(file_path, dayfirst=True)
    
    # Drop unnecessary columns
    df.drop(['Number', 'Account'], axis=1, inplace=True)
    
    df.rename(columns={'Memo': 'Entity'
    }, inplace=True)
    
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y').dt.strftime('%d/%m/%Y')
    
    df['Entity'] = df['Entity'].str.strip().replace('\s+', ' ', regex=True)
    
    df['Category'] = ''
    
    df = df[['Date', 'Amount', 'Subcategory', 'Entity', 'Category']]
    
    return df

def process_files(raw_data_dir, clean_data_dir, finished_dir):
    # Ensure the clean data and finished data directories exist
    os.makedirs(clean_data_dir, exist_ok=True)
    os.makedirs(finished_dir, exist_ok=True)
    
    # Iterate through each file in the raw data directory
    for file_name in os.listdir(raw_data_dir):
        if file_name.endswith('.csv') and 'Barclays' in file_name:  # Process only CSV files with 'Barclays' in the filename
            print(f"Processing {file_name}...")
            file_path = os.path.join(raw_data_dir, file_name)
            
            # Clean the data
            cleaned_df = clean_barclays_data(file_path)
            
            # Construct new file name and path for cleaned data
            new_file_name = f"(new){file_name}"
            new_file_path = os.path.join(clean_data_dir, new_file_name)
            
            # Save the cleaned data to the new file
            cleaned_df.to_csv(new_file_path, index=False, date_format='%d/%m/%Y')
            print(f"Cleaned data saved to {new_file_name}")
            
            # Move the original file to the finished directory
            finished_file_path = os.path.join(finished_dir, file_name)
            shutil.move(file_path, finished_file_path)
            print(f"Moved processed file to {finished_file_path}")


if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get the directory of the project root by navigating up from the script directory
    project_dir = os.path.dirname(script_dir)
    
    # Define the raw_data_dir and clean_data_dir relative to the project directory
    raw_data_dir = os.path.join(project_dir, 'data', 'raw data')
    clean_data_dir = os.path.join(project_dir, 'data', 'clean data')
    finished_dir = os.path.join(raw_data_dir, 'finished')  # Subfolder for finished files
    
    process_files(raw_data_dir, clean_data_dir, finished_dir)
    print("Data cleaning processed completed successfully")
