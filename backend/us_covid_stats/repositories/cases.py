from typing import Iterable, TypedDict

from us_covid_stats.infrastructure.dynamodb import (
    batch_put_item,
    query_all,
)


class CaseData(TypedDict):
    date: str
    cases: int
    deaths: int
    recoveries: int


CASES_PK = "CASES"


def get_all_cases() -> Iterable[CaseData]:
    for case in query_all(pk=CASES_PK):
        yield CaseData(
            date=case["sk"],
            cases=case["cases"],
            deaths=case["deaths"],
            recoveries=case["recoveries"],
        )


def save_cases(cases: Iterable[CaseData]) -> None:
    return batch_put_item(
        {
            "pk": CASES_PK,
            "sk": case["date"],
            "cases": case["cases"],
            "deaths": case["deaths"],
            "recoveries": case["recoveries"],
        }
        for case in cases
    )
