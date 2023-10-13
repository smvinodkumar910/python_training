from google.cloud import storage

storage_client = storage.Client("bamboo-bulwark-319114")

def upload_with_filename():
    bucket = storage_client.bucket("cit_project")
    blob = bucket.blob("upload/Financial_Sample_from_gcs.csv")

    source_file_name = 'c:/Users/smvin/Documents/Python_training/Financial_Sample_from_gcs.csv'

    blob.upload_from_filename(source_file_name)

def upload_with_string():
    bucket = storage_client.bucket("cit_project")
    contents ="Test file content"
    blob = bucket.blob("upload/uploaded_with_string.txt")
    blob.upload_from_string(contents)

def rename_blob():
    bucket = storage_client.bucket("cit_project")
    blob = bucket.blob("upload/uploaded_with_string.txt")

    new_blob = bucket.rename_blob(blob, "upload/uploaded_with_string_renamed.txt")


rename_blob()
