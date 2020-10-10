from io import StringIO
from typing import Any

import boto3
from us_covid_stats.config.settings import DATA_BUCKET

s3 = boto3.resource("s3")


def save_to_data_bucket(key: str, buffer: StringIO) -> Any:
    return s3.Object(DATA_BUCKET, key).put(Body=buffer.getvalue())


def retrieve_from_data_bucket(key: str) -> Any:
    return s3.Object(DATA_BUCKET, key).get().get("Body")
