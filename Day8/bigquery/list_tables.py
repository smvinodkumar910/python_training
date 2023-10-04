from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client("bamboo-bulwark-319114")

# TODO(developer): Set dataset_id to the ID of the dataset that contains
#                  the tables you are listing.
# dataset_id = 'your-project.your_dataset'

tables = client.list_tables("bamboo-bulwark-319114.kazi_1")  # Make an API request.

print("Tables contained in '{}':".format("bamboo-bulwark-319114.kazi_1"))
for table in tables:
    print("{}.{}.{}".format(table.project, table.dataset_id, table.table_id))