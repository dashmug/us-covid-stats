from typing import TypedDict

from pandas import DataFrame, read_csv
from us_covid_stats.config.settings import US_CASES_URL, WORLD_RECOVERIES_URL


class ExtractedData(TypedDict):
    cases: DataFrame
    recoveries: DataFrame


def extract_data_from_sources() -> ExtractedData:
    us_cases: DataFrame = read_csv(
        US_CASES_URL,
        index_col="date",
        parse_dates=True,
    )
    world_recoveries: DataFrame = read_csv(
        WORLD_RECOVERIES_URL,
        usecols=["Date", "Country/Region", "Recovered"],
        index_col="Date",
        parse_dates=True,
    )
    is_us_recovery = world_recoveries["Country/Region"] == "US"
    us_recoveries = world_recoveries[is_us_recovery].drop(columns=["Country/Region"])

    return {
        "cases": us_cases,
        "recoveries": us_recoveries,
    }
