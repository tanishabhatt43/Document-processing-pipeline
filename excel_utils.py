import pandas as pd

def process_excel(file_path):
    df = pd.read_excel(file_path)
    return {
        "type": "excel",
        "columns": list(df.columns),
        "rows": df.fillna("").values.tolist()
    }
