from collections import Callable, Iterable, Mapping

from pandas import DataFrame
from us_covid_stats.infrastructure.api_gateway import Response
from us_covid_stats.repositories.cases import CaseData
from us_covid_stats.rest.helpers import create_response_from_dataframe


def handle_data(cases: Iterable[CaseData]) -> Response:
    df = DataFrame(cases)

    return create_response_from_dataframe(df)


def handle_daily(cases: Iterable[CaseData]) -> Response:
    df = DataFrame(cases).set_index("date").diff().reset_index()

    return create_response_from_dataframe(df)


def handle_weekly(cases: Iterable[CaseData]) -> Response:
    df = (
        DataFrame(cases)
        .astype({"date": "datetime64"})
        .set_index("date")
        .diff()
        .resample("W")
        .sum()
        .reset_index()
    )
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")

    return create_response_from_dataframe(df)


def handle_monthly(cases: Iterable[CaseData]) -> Response:
    df = (
        DataFrame(cases)
        .astype({"date": "datetime64"})
        .set_index("date")
        .diff()
        .resample("M")
        .sum()
        .reset_index()
    )
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")

    return create_response_from_dataframe(df)


router: Mapping[str, Callable[[Iterable[CaseData]], Response]] = {
    "/data": handle_data,
    "/daily": handle_daily,
    "/weekly": handle_weekly,
    "/monthly": handle_monthly,
}
