from google.cloud import storage

from google.cloud import storage


def create_bucket_class_location(bucket_name):
    """
    Create a new bucket in the US region with the coldline storage
    class
    """
    # bucket_name = "your-new-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print(
        "Created bucket {} in {} with storage class {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket
#creating bucket
create_bucket_class_location("btw-aiml-gcp2026-batch")


print("*"*50)
print("Creating  folder")
print("*"*50)
# creating folder
from google.cloud import storage

def create_folder(bucket_name, folder_name):
    client = storage.Client()

    bucket = client.bucket(bucket_name)

    blob = bucket.blob(folder_name + "/")
    blob.upload_from_string("")

    print("Folder created")

create_folder("gcp-aiml-dipali-bucket","Folder1")

print("*"*50)
print("list")
print("*"*50)

#List of buckets
from google.cloud import storage

def list_buckets():
    client = storage.Client()

    for bucket in client.list_buckets():
        print(bucket.name)
list_buckets()


print("*"*50)
print("uploading file")
print("*"*50)
#upload file 
from google.cloud import storage

def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
    """Uploads a file to the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(contents)

    print(
        f"{destination_blob_name} with contents {contents} uploaded to {bucket_name}."
    )
upload_blob_from_memory("gcp-aiml-dipali-bucket","D:/brainworks sql file/Assignment.docx","D:/brainworks sql file/Assignment.docx")

print("*"*50)
print("Creating another bucket")
print("*"*50)
def create_bucket_class_location(bucket_name):
    """
    Create a new bucket in the US region with the coldline storage
    class
    """
    # bucket_name = "your-new-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print(
        "Created bucket {} in {} with storage class {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket
#creating bucket
create_bucket_class_location("btw-aiml-gcp2026-batch")


print("*"*50)
print("Creating another folder")
print("*"*50)
def create_folder(bucket_name, folder_name):
    client = storage.Client()

    bucket = client.bucket(bucket_name)

    blob = bucket.blob(folder_name + "/")
    blob.upload_from_string("")

    print("Folder created")

create_folder("gcp-aiml-dipali-bucket1","Folder2")



print("*"*50)
print("Copy file")
print("*"*50)
#copy file
def copy_file(bucket_name, source_file, destination_file):
    client = storage.Client()

    bucket = client.bucket(bucket_name)

    source_blob = bucket.blob(source_file)

    bucket.copy_blob(
        source_blob,
        bucket,
        destination_file
    )

    print("File copied")

copy_file("gcp-aiml-dipali-bucket","D:/brainworks sql file/Assignment.docx",'gcp-aiml-dipali-bucket1')


print("*"*50)
print("Move file")
print("*"*50)
#move file
def move_file(bucket_name, source_file, destination_file):
    client = storage.Client()

    bucket = client.bucket(bucket_name)

    source_blob = bucket.blob(source_file)

    bucket.copy_blob(
        source_blob,
        bucket,
        destination_file
    )

    source_blob.delete()

    print("File moved")

move_file("gcp-aiml-dipali-bucket","D:/brainworks sql file/Assignment.docx",'gcp-aiml-dipali-bucket1')

'''
print("*"*50)
print("Delete file")
print("*"*50)
#Delete file
def delete_file(bucket_name, file_name):
    client = storage.Client()

    bucket = client.bucket(bucket_name)

    blob = bucket.blob(file_name)
    blob.delete()

    print("File deleted")

delete_file("gcp-aiml-dipali-bucket","D:/brainworks sql file/Assignment.docx")


print("*"*50)
print("delete bucket")
print("*"*50)
#Delete Bucket
def delete_bucket(bucket_name):
    client = storage.Client()

    bucket = client.bucket(bucket_name)

    bucket.delete()

    print(f"Bucket {bucket_name} deleted")
delete_bucket("gcp-aiml-dipali-bucket")'''