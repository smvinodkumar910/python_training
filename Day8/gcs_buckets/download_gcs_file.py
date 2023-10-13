from google.cloud import storage

storage_client = storage.Client("bamboo-bulwark-319114")

bucket = storage_client.bucket("cit_project")

# Construct a client side representation of a blob.
# Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
# any content from Google Cloud Storage. As we don't need additional data,
# using `Bucket.blob` is preferred here.
blob = bucket.blob("Financial Sample.csv")
blob.download_to_filename("Financial_Sample_from_gcs.csv")


