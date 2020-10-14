from typing import Any, TypedDict

from us_covid_stats.etl.extract import extract_data_from_sources
from us_covid_stats.etl.load import load_data_to_database
from us_covid_stats.etl.transform import merge_cases_with_recoveries
from us_covid_stats.infrastructure.logging import log_event, logger
from us_covid_stats.infrastructure.sns import notify


def refresh_data_from_sources(event: Any, context: Any) -> str:
    extracted = extract_data_from_sources()
    transformed = merge_cases_with_recoveries(**extracted)

    return load_data_to_database(transformed)


class RequestContext(TypedDict):
    condition: str


class DestinationEvent(TypedDict):
    requestContext: RequestContext
    responsePayload: str


@log_event
def on_refresh_data_from_sources(event: DestinationEvent, context: Any) -> None:
    notify(
        message=event["responsePayload"],
        condition=event["requestContext"]["condition"],
    )
