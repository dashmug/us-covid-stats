from io import StringIO
from typing import Any

import boto3
from us_covid_stats.config.settings import DATA_BUCKET

s3 = boto3.resource("s3")


def save_to_data_bucket(key: str, buffer: StringIO) -> Any:
    return s3.Object(DATA_BUCKET, key).put(Body=buffer.getvalue())


class MissingFileError(Exception):
    def __init__(self, key: str, message: str = "File Not Found"):
        self.key = key
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f"{self.message}: {self.key}"


def retrieve_from_data_bucket(key: str) -> Any:
    try:
        return s3.Object(DATA_BUCKET, key).get().get("Body")
    except s3.meta.client.exceptions.NoSuchKey:
        raise MissingFileError(key)
