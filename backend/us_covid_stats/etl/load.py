from pandas import DataFrame

from us_covid_stats.repositories.cases import CaseData, save_cases
from us_covid_stats.repositories.csv import get_csv, save_csv


def load_data_to_database(latest_data: DataFrame) -> None:
    old_data: DataFrame = get_csv()

    difference = (
        old_data.merge(
            latest_data,
            how="outer",
            on=["date", "cases", "deaths", "recoveries"],
            indicator=True,
        )
        .loc[lambda x: x["_merge"] == "right_only"]
        .drop("_merge", axis=1)
    )

    save_cases(
        CaseData(
            date=row.Index.strftime("%Y-%m-%d"),
            cases=row.cases,
            deaths=row.deaths,
            recoveries=row.recoveries,
        )
        for row in difference.itertuples()
    )
    save_csv(latest_data)
