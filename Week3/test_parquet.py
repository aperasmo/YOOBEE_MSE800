import pandas as pd

file_path = "Week3\TestPad_PCB_XYRGB_V2_Output.parquet"

try:
    df = pd.read_parquet(file_path, engine="pyarrow")
    print("✅ This is a valid Parquet file.")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print(df.head())
except Exception as e:
    print("❌ Not a valid Parquet file:", e)
    