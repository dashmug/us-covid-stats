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

    date_column = "Date"
    country_region_column = "Country/Region"
    recovered_column = "Recovered"

    world_recoveries: DataFrame = read_csv(
        WORLD_RECOVERIES_URL,
        usecols=[date_column, country_region_column, recovered_column],
        index_col=date_column,
        parse_dates=True,
    )
    is_us_recovery = world_recoveries[country_region_column] == "US"
    us_recoveries = world_recoveries[is_us_recovery].drop(
        columns=[country_region_column]
    )

    return {
        "cases": us_cases,
        "recoveries": us_recoveries,
    }
