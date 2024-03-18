from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client("mynewdevenv")

# TODO(developer): Set dataset_id to the ID of the dataset that contains
#                  the tables you are listing.
# dataset_id = 'your-project.your_dataset'

tables = client.list_tables("mynewdevenv.dbt_madhavan")  # Make an API request.

print("Tables contained in '{}':".format("mynewdevenv.dbt_madhavan"))
for table in tables:
    print("{}.{}.{}".format(table.project, table.dataset_id, table.table_id))