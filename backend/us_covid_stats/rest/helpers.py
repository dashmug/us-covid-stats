from pandas import DataFrame
from us_covid_stats.infrastructure.api_gateway import Response, create_response


def create_response_from_dataframe(df: DataFrame) -> Response:
    return create_response(
        df.fillna(0)
        .astype({"cases": "int", "deaths": "int", "recoveries": "int"})
        .to_json(orient="records"),
        content_type="application/json",
    )
