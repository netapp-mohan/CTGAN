import pandas as pd

file_path = '/Users/macharya/Downloads/CTGAN/2000Q1.csv'
df = pd.read_csv(file_path, sep = '|')

num_columns = len(df.columns)
col_labels = [str(i) for i in range(num_columns)]
df.columns = col_labels 

excluded_columns = ['3','4','5','25','26','27','29','30','34','35','36','41','73','80','86','102']

# Replace 'XX' with 0 in numeric columns, excluding specific columns
numeric_columns = df.select_dtypes(include=[float, int]).columns
for col in range(len(numeric_columns)):
    if col not in excluded_columns:
        df[numeric_columns[col]] = df[numeric_columns[col]].replace('XX', 0)

df.fillna(0, inplace=True)
df.iloc[:,41].replace('XX',0, inplace=True)
df.iloc[:,101].replace('XX',0, inplace=True)
df.iloc[:,105].replace('XX',0, inplace=True)

df.to_csv('new_data_path.csv')
