from google.cloud import storage

storage_client = storage.Client("mynewdevenv")

bucket = storage_client.bucket("mynewdevenv-bucket")

# Construct a client side representation of a blob.
# Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
# any content from Google Cloud Storage. As we don't need additional data,
# using `Bucket.blob` is preferred here.
blob = bucket.blob("sample/us-states.csv")
blob.download_to_filename("us-states-downloaded.csv")




