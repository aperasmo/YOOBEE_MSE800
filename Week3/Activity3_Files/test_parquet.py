import pandas as pd

# This script checks if a given file is a valid Parquet file and prints its contents.
file_path = "Week3\Activity3_Files\TestPad_PCB_XYRGB_V2_Output.parquet" # Path to the Parquet file

try:
    df = pd.read_parquet(file_path, engine="pyarrow") # Read the Parquet file using pyarrow engine
    print("This is a valid Parquet file.")
    print("Shape:", df.shape) # Print the shape of the DataFrame
    print("Columns:", df.columns.tolist()) # Print the first few rows of the DataFrame
    print(df.head()) # Print the first few rows of the DataFrame
except Exception as e:
    print("Not a valid Parquet file:", e)   
