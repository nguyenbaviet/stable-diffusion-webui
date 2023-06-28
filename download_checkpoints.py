import os

from google.cloud import storage

gcs_model_path = 'wedjat/models/stable_diffusion/models'
des_path = 'models'
os.makedirs(des_path, exist_ok=True)

client = storage.Client(project='momovn-dev')
bucket = client.bucket('momovn-models-dev')
blobs = bucket.list_blobs(prefix=gcs_model_path)
total = len(blobs)
for idx, blob in enumerate(blobs):
    filename = blob.name.split("/")[-1]
    print(f"downloading {idx}/{total}: {filename}")
    destination_file_path = os.path.join(des_path, filename)
    blob.download_to_filename(destination_file_path)
