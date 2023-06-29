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
    par_dir, filename = filename
    des_dir = os.path.join(des_path, par_dir)
    os.makedirs(des_dir, exist_ok=True)
    print(f"downloading {filename}")
    blob.download_to_filename(os.path.join(des_dir, filename))
# cp weight to Lora extensions
os.makedirs("/stable-diffusion-webui/extensions/sd-webui-additional-networks/models", exist_ok=True)
os.system("cp -r /stable-diffusion-webui/models/Lora /stable-diffusion-webui/extensions/sd-webui-additional-networks/models")
