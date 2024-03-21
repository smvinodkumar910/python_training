from google.cloud import storage

storage_client = storage.Client("mynewdevenv")

def upload_with_filename():
    bucket = storage_client.bucket("mynewdevenv-bucket")
    blob = bucket.blob("sample/upload/Financial_Sample_from_gcs.csv")

    source_file_name = 'c:/Users/smvin/Documents/Python_training/Financial_Sample_from_gcs.csv'

    blob.upload_from_filename(source_file_name)

def upload_with_string():
    bucket = storage_client.bucket("mynewdevenv-bucket")
    contents ="Test file content"
    blob = bucket.blob("sample/upload/uploaded_with_string.txt")
    blob.upload_from_string(contents)

def rename_blob():
    bucket = storage_client.bucket("mynewdevenv-bucket")
    blob = bucket.blob("sample/upload/uploaded_with_string.txt")

    new_blob = bucket.rename_blob(blob, "sample/upload/uploaded_with_string_renamed.txt")


rename_blob()
