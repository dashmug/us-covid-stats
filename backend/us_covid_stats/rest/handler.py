import json
from typing import Any, Mapping, TypedDict

from us_covid_stats.infrastructure.api_gateway import create_response
from us_covid_stats.infrastructure.logging import log_event
from us_covid_stats.repositories.cases import get_all_cases
from us_covid_stats.rest.routes import router


class Event(TypedDict):
    rawPath: str


@log_event
def get_data(event: Event, context: Any) -> Mapping[str, Any]:
    cases = list(get_all_cases())

    if not cases:
        return create_response(json.dumps([]), content_type="application/json")

    handler = router.get(event["rawPath"])

    if handler:
        return handler(cases)

    return create_response(json.dumps([]), content_type="application/json")
