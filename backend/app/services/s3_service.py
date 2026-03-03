import boto3
import os
from botocore.exceptions import NoCredentialsError

class S3Service:
    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
        )
        self.bucket = os.getenv("S3_BUCKET")

    def upload_file(self, file_path: str, s3_key: str):
        try:
            self.s3.upload_file(file_path, self.bucket, s3_key)
            return f"https://{self.bucket}.s3.amazonaws.com/{s3_key}"
        except NoCredentialsError:
            raise Exception("S3 credentials not configured")

    def generate_signed_url(self, s3_key: str, expires=600):
        return self.s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": self.bucket, "Key": s3_key},
            ExpiresIn=expires,
        )