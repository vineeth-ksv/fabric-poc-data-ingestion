from azure.storage.blob import BlobClient, StorageStreamDownloader

def read_file(
    connection: str, container: str, filename: str
) -> StorageStreamDownloader:
    blob = BlobClient.from_connection_string(
        conn_str=connection,
        container_name=container,
        blob_name=filename,
    )

    return blob.download_blob()


def write_to_file(connection: str, container: str, filename: str, content: bytes):
    blob = BlobClient.from_connection_string(
        conn_str=connection,
        container_name=container,
        blob_name=filename,
    )
    if blob.exists():
        blob.delete_blob()
    blob.upload_blob(data=content)