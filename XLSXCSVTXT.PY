import pandas as pd
import numpy as np
import os
from datetime import datetime

def convert_file(input_path, output_path, output_format):
    if output_format == 'csv':
        df.to_csv(output_path, index=False)
    elif output_format == 'xlsx':
        df.to_excel(output_path, index=False)
    elif output_format == 'txt':
        df.to_csv(output_path, index=False, sep='\t')

# Get user input for the file path
file_path = input("Please provide the path to the file you want to convert: ")

# Determine file format
file_format = file_path.split('.')[-1]

# Read the file using Pandas
if file_format == 'csv':
    # Read with low_memory=False to suppress the DtypeWarning
    df = pd.read_csv(file_path, low_memory=False)
elif file_format == 'xlsx':
    df = pd.read_excel(file_path, engine='openpyxl')
elif file_format == 'txt':
    df = pd.read_csv(file_path, sep='\t', low_memory=False)

# Ask the user for the desired output format
output_format = input("Please specify the desired output format (csv, xlsx, or txt): ")

# Generate the output file name with the specified format and timestamp
timestamp = datetime.now().strftime('%d%b%y')
output_file_name = os.path.splitext(os.path.basename(file_path))[0] + f'-{output_format.upper()}-{timestamp}.{output_format}'

# Specify the output path
output_path = os.path.join(os.path.dirname(file_path), output_file_name)

# Perform the conversion
convert_file(file_path, output_path, output_format)

print(f"Conversion successful! Output file: {output_path}")