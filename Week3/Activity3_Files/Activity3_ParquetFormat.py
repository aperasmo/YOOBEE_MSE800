# Week 3 Activity 3: Parquet Format Conversion and Analysis
# Develop a Python project using an object-oriented (OO) approach to convert large datasets into Parquet format.
# Then, compute the maximum, minimum, average, and absolute values for each column in the dataset.
# Finally, share the GitHub repository link along with a screenshot of the results. 

import io # Import io for handling file operations
import pandas as pd # Import pandas for data manipulation
import pyarrow as pa # Import pyarrow for Parquet file handling
import pyarrow.parquet as pq # Import pyarrow's Parquet module for reading/writing Parquet files

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path # Initialize with the file path
        self.data = None        # Placeholder for the DataFrame

    def load_csv(self):
        #Load CSV file into pandas DataFrame
        self.data = pd.read_csv(self.file_path)
        print("CSV file loaded successfully!")

    def save_to_parquet(self, output_file):
        #Save DataFrame into Parquet format
        if self.data is not None:
            self.data.to_parquet(output_file, engine="pyarrow", index=False)
            print(f"Data saved to {output_file}")
        else:
            print("No data to save!")

    def compute_statistics(self):
        #Compute max, min, mean, and absolute values per column
        if self.data is not None:
            stats = pd.DataFrame({
                "Max": self.data.max(),
                "Min": self.data.min(),
                "Average": self.data.mean(),
                "Absolute": self.data.abs().sum()
            })
            print("\nColumn Statistics:\n")
            print(stats)
            return stats
        else:
            print("No data loaded!")
            return None


if __name__ == "__main__":
    # Change this to your downloaded CSV file path
    csv_file = "Week3\Activity3_Files\TestPad_PCB_XYRGB_V2.csv"
    parquet_file = "Week3\Activity3_Files\TestPad_PCB_XYRGB_V2_Output.parquet" # Output Parquet file path

    processor = DataProcessor(csv_file)

    # Step 1: Load CSV
    processor.load_csv()

    # Step 2: Save to Parquet
    processor.save_to_parquet(parquet_file)

    # Step 3: Compute Stats
    results = processor.compute_statistics()