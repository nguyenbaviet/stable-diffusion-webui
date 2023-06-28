import os

from google.cloud import storage

gcs_model_path = 'wedjat/models/stable_diffusion/models'
des_path = 'models'
os.makedirs(des_path, exist_ok=True)

print("Connect to gcs")
client = storage.Client(project='momovn-dev')
bucket = client.bucket('momovn-models-dev')
blobs = bucket.list_blobs(prefix=gcs_model_path)
print("Start downloading...")
for blob in blobs:
    filename = blob.name.split("/")[-2:]
    filename = "/".join(filename)
    destination_file_path = os.path.join(des_path, filename)
    os.makedirs(destination_file_path, exist_ok=True)
    print(f"downloading {filename}")
    blob.download_to_filename(destination_file_path)
