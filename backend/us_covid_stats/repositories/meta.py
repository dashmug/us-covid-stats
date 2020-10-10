from typing import Optional

from us_covid_stats.infrastructure.dynamodb import get_item, put_item

META = "META"

CASES_LATEST_DATE = "CASES:LATEST_DATE"


def get_cases_latest_date() -> Optional[str]:
    item = get_item(pk=META, sk=CASES_LATEST_DATE)

    return item.get("latest_date") if item else None


def update_cases_latest_date(date_str: str) -> None:
    put_item(
        pk=META,
        sk=CASES_LATEST_DATE,
        latest_date=date_str,
    )
