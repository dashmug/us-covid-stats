import os

SERVICE_NAME = os.getenv("SERVICE_NAME", default="us-covid-stats")
STAGE = os.getenv("STAGE", default="main")
AWS_REGION = os.getenv("AWS_REGION", default="us-east-1")

RAW_GITHUB_HOST = "https://raw.githubusercontent.com"

# New York Times Data
US_CASES_URL = f"{RAW_GITHUB_HOST}/nytimes/covid-19-data/master/us.csv"

# John Hopkins Data
WORLD_RECOVERIES_URL = (
    f"{RAW_GITHUB_HOST}/datasets/covid-19/master/data/time-series-19-covid-combined.csv"
)

DATA_TABLE = os.getenv("DATA_TABLE")
DATA_BUCKET = os.getenv("DATA_BUCKET")

NOTIFICATION_TOPIC = os.getenv("NOTIFICATION_TOPIC")
