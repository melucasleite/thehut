from google.cloud import storage


class GoogleStorage:

    def __init__(self, bucket_name):
        self.storage_client = storage.Client.from_service_account_json(
            'credentials-storage-admin.json')
        self.bucket_name = bucket_name

    def create_bucket(self):
        """Creates a new bucket."""
        bucket = self.storage_client.create_bucket(self.bucket_name)
        print('Bucket {} created'.format(bucket.name))

    def delete_bucket(self):
        """Deletes a bucket. The bucket must be empty."""
        bucket = self.storage_client.get_bucket(self.bucket_name)
        bucket.delete()
        print('Bucket {} deleted'.format(bucket.name))

    def list_buckets(self):
        """List Buckets."""
        return self.storage_client.list_buckets()

    def list_buckets_names(self):
        """List Buckets."""
        return [bucket.name for bucket in self.storage_client.list_buckets()]

    def list_blobs(self):
        """Lists all the blobs in the bucket."""
        bucket = self.storage_client.get_bucket(self.bucket_name)

        return bucket.list_blobs()

    def upload_file(self, file_stream, filename, content_type):
        """
        Uploads a file to a given Cloud Storage bucket and returns the public url
        to the new object.
        """

        client = self.storage_client
        bucket = client.bucket(self.bucket_name)
        blob = bucket.blob(filename)

        blob.upload_from_string(
            file_stream,
            content_type=content_type)

        blob.make_public()

        url = blob.public_url

        import six
        if isinstance(url, six.binary_type):
            url = url.decode('utf-8')

        return url

    def delete_blob(self, blob_name):
        """Deletes a blob from the bucket."""
        bucket = self.storage_client.get_bucket(self.bucket_name)
        blob = bucket.blob(blob_name)

        return blob.delete()
