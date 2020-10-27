import json
from typing import Any, Mapping, TypedDict, Union

from us_covid_stats.etl.extract import extract_data_from_sources
from us_covid_stats.etl.load import load_data_to_database
from us_covid_stats.etl.transform import merge_cases_with_recoveries
from us_covid_stats.infrastructure.logging import log_event
from us_covid_stats.infrastructure.sns import notify


@log_event
def refresh_data_from_sources(event: Any, context: Any) -> str:
    extracted = extract_data_from_sources()
    transformed = merge_cases_with_recoveries(**extracted)

    return load_data_to_database(transformed)


class RequestContext(TypedDict):
    condition: str


class DestinationEvent(TypedDict):
    requestContext: RequestContext
    responsePayload: Union[str, Mapping[str, Any]]


@log_event
def on_refresh_data_from_sources(event: DestinationEvent, context: Any) -> None:
    if isinstance(event["responsePayload"], dict):
        message = json.dumps(event["responsePayload"].get("errorMessage"))
    else:
        message = event["responsePayload"]
    notify(
        message=message,
        condition=event["requestContext"]["condition"],
    )
