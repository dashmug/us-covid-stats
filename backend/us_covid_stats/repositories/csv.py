from io import StringIO
from typing import Any

from pandas import DataFrame, read_csv
from us_covid_stats.infrastructure.s3 import (
    retrieve_from_data_bucket,
    save_to_data_bucket,
)

CSV_FILENAME = "data.csv"


def save_csv(df: DataFrame) -> Any:
    buffer = StringIO()
    df.to_csv(buffer)

    return save_to_data_bucket(CSV_FILENAME, buffer)


def get_csv() -> DataFrame:
    return read_csv(
        retrieve_from_data_bucket(CSV_FILENAME),
        index_col="date",
        parse_dates=True,
    )
