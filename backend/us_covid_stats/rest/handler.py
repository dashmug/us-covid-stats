import json
from typing import Any, Mapping, TypedDict

from pandas import DataFrame
from us_covid_stats.infrastructure.api_gateway import create_response
from us_covid_stats.infrastructure.logging import log_event
from us_covid_stats.repositories.cases import get_all_cases
from us_covid_stats.rest.helpers import create_response_from_dataframe


class Event(TypedDict):
    rawPath: str


@log_event
def get_data(event: Event, context: Any) -> Mapping[str, Any]:
    cases = list(get_all_cases())

    if not cases:
        return create_response(json.dumps([]), content_type="application/json")

    if event["rawPath"] == "/data":
        df = DataFrame(cases)

        return create_response_from_dataframe(df)

    if event["rawPath"] == "/daily":
        df = DataFrame(cases).set_index("date").diff().reset_index()

        return create_response_from_dataframe(df)

    if event["rawPath"] == "/weekly":
        df = DataFrame(cases).set_index("date").diff().resample("W").reset_index()

        return create_response_from_dataframe(df)

    if event["rawPath"] == "/monthly":
        df = DataFrame(cases).set_index("date").diff().resample("M").reset_index()

        return create_response_from_dataframe(df)

    return create_response(json.dumps([]), content_type="application/json")
