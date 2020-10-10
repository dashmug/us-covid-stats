from typing import Any, Mapping

from pandas import DataFrame
from us_covid_stats.infrastructure.api_gateway import create_response
from us_covid_stats.repositories.cases import get_all_cases


def get_data(event: Any, context: Any) -> Mapping[str, Any]:
    df = DataFrame(list(get_all_cases())).fillna(0)

    return create_response(
        df.to_json(orient="records"), content_type="application/json"
    )
