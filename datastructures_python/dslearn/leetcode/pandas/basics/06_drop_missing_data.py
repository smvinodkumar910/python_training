import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset='name',axis=0)

data = [
    {"student_id": 1, "name": "Alice", "age": 15},
    {"student_id": 2, "name": "Bob", "age": 16},
    # Add more data entries here following the same format
]

# Define the column names and data types from the table
column_names = ["student_id", "name", "age"]
data_types = {"student_id": int, "name": object, "age": int}

# Create the DataFrame using pd.DataFrame() with data type specification
df = pd.DataFrame(data, columns=column_names)

print(dropMissingData(df))