import pandas as pd
# import fastparquet as fp #in case if fastparquet doesn't work

# Set file paths
csv_file = 'hrdata.csv'
parquet_file = 'hrdata.parquet'

# Read CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Write DataFrame to Parquet file
df.to_parquet(parquet_file)

# Using "fastparquet", which are the two libraries that Pandas can use to read and write Parquet files: to install use <pip install fastparquet> or <pip install --user fastparquet>

