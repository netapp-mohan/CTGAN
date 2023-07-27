import pandas as pd

# Provide the file path of your input CSV file
#file_path = '/Users/macharya/Downloads/CTGAN/sf-loan-performance-data-sample.csv'
file_path = '/Users/macharya/Downloads/CTGAN/2000Q1.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, sep='|')
df.fillna(0, inplace=True)
num_columns = len(df.columns)
col_labels = [str(i) for i in range(num_columns)]
df.columns = col_labels 
columns_to_drop = []
for column in df.columns:
    if all(df[column] == 0):
        columns_to_drop.append(column)
df = df.drop(columns=columns_to_drop)
# Filter out rows that contain 'XX' in any of the columns
filtered_df = df[~df.apply(lambda row: row.astype(str).str.contains('XX')).any(axis=1)]

# Provide the file path for the output CSV file
output_file_path = '/Users/macharya/Downloads/CTGAN/reduced_data.csv'

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv(output_file_path, index=False)
