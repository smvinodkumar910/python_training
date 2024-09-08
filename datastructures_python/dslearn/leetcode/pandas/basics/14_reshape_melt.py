import pandas as pd

data = {
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
}

# Create the DataFrame from the dictionary
df = pd.DataFrame(data)

print(df)

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt( id_vars=['product'], value_vars=['quarter_1','quarter_2','quarter_3','quarter_4'], ignore_index=True, value_name='sales',var_name='quarter')
    

print(meltTable(df))