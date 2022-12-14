import os, uuid
import ini
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from azure.storage.queue import QueueServiceClient, QueueClient
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
credential={
    "account_name": ini.account_name,
    "account_key": ini.account_key
}
# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient(ini.blobsc,credential)


def send_message_queue(timestamp):
    queue = QueueClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=uploadfilesfrom1;AccountKey=1e7X5xrSXCf5FkBFB8yVG4XA+PFtnmzk0YkXXRN8jrcbri4WsE8G6kxI5l7FAo7G6D2wk+sBde9/+AStNFEScA==;EndpointSuffix=core.windows.net", queue_name="uploadfiles")
    queue.send_message(timestamp)

        
def upload_to_blob(file, filename): #upload the file to the Files blob,
    blob_client = blob_service_client.get_blob_client(ini.container, blob=filename) 
    blob_client.upload_blob(file)


def blob_to_file(cont,filename):
    blob_client = blob_service_client.get_blob_client(container=cont, blob=filename) 
    with open (ini.filelocation, "wb") as myblob:
        blob_data = blob_client.download_blob()
        blob_data.readinto(myblob)