from typing import Any

from us_covid_stats.etl.extract import extract_data_from_sources
from us_covid_stats.etl.load import load_data_to_database
from us_covid_stats.etl.transform import merge_cases_with_recoveries


def refresh_data_from_sources(event: Any, context: Any) -> str:
    extracted = extract_data_from_sources()
    transformed = merge_cases_with_recoveries(**extracted)

    return load_data_to_database(transformed)
