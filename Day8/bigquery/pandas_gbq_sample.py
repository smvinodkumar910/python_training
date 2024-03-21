import pandas
import pandas_gbq

# TODO: Set project_id to your Google Cloud Platform project ID.
project_id = "mynewdevenv"

# TODO: Set table_id to the full destination table ID (including the
#       dataset ID).
table_id = 'python_learning_demo.dataframe_tb'

df = pandas.DataFrame(
    {
        "my_string": ["a", "b", "c"],
        "my_int64": [1, 2, 3],
        "my_float64": [4.0, 5.0, 6.0],
        "my_bool1": [True, False, True],
        "my_bool2": [False, True, False],
        "my_dates": pandas.date_range("now", periods=3),
    }
)

#pandas_gbq.to_gbq(df, table_id, project_id=project_id)

bqdf = pandas_gbq.read_gbq(query_or_table="python_learning_demo.us_states",project_id="mynewdevenv")
print(bqdf)