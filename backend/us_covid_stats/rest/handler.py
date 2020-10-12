from typing import Any, Mapping

from pandas import DataFrame
from us_covid_stats.infrastructure.api_gateway import create_response
from us_covid_stats.infrastructure.logging import log_event
from us_covid_stats.repositories.cases import get_all_cases


@log_event
def get_data(event: Any, context: Any) -> Mapping[str, Any]:
    df = DataFrame(list(get_all_cases()))

    return create_response(
        df.fillna(0)
        .astype({"cases": "int", "deaths": "int", "recoveries": "int"})
        .to_json(orient="records"),
        content_type="application/json",
    )


def get_daily(event: Any, context: Any) -> Mapping[str, Any]:
    df = DataFrame(list(get_all_cases())).set_index("date").diff().reset_index()

    return create_response(
        df.fillna(0)
        .astype({"cases": "int", "deaths": "int", "recoveries": "int"})
        .to_json(orient="records"),
        content_type="application/json",
    )


def get_weekly(event: Any, context: Any) -> Mapping[str, Any]:
    df = (
        DataFrame(list(get_all_cases()))
        .set_index("date")
        .diff()
        .resample("W")
        .reset_index()
    )

    return create_response(
        df.fillna(0)
        .astype({"cases": "int", "deaths": "int", "recoveries": "int"})
        .to_json(orient="records"),
        content_type="application/json",
    )


def get_monthly(event: Any, context: Any) -> Mapping[str, Any]:
    df = (
        DataFrame(list(get_all_cases()))
        .set_index("date")
        .diff()
        .resample("M")
        .reset_index()
    )

    return create_response(
        df.to_json(orient="records"), content_type="application/json"
    )
