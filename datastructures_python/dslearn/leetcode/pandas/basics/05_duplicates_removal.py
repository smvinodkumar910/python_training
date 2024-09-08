import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    #customers.drop_duplicates(subset='email',keep="first",inplace=True)
    customers['dup'] = customers.duplicated(subset='email',keep="first")
    return customers
    



data = [
    ["1", "Ella", "emily@example.com"],
    ["2", "David", "michael@example.com"],
    ["3", "Zachary", "sarah@example.com"],
    ["4", "Alice", "john@example.com"],
    ["5", "Finn", "john@example.com"],
    ["6", "Violet", "alice@example.com"],
]

# Define column names
column_names = ["customer_id", "name", "email"]

# Create DataFrame
df = pd.DataFrame(data, columns=column_names)

print(dropDuplicateEmails(df))