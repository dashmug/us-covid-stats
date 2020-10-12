from pandas import DataFrame

from us_covid_stats.infrastructure.s3 import MissingFileError
from us_covid_stats.repositories.cases import CaseData, save_cases
from us_covid_stats.repositories.csv import s3_csv_to_dataframe, dataframe_to_s3_csv


def load_data_to_database(latest_data: DataFrame) -> str:
    try:
        old_data: DataFrame = s3_csv_to_dataframe()
    except MissingFileError:
        df = latest_data
    else:
        df = (
            old_data.merge(
                latest_data,
                how="outer",
                on=["date", "cases", "deaths", "recoveries"],
                indicator=True,
            )
            .loc[lambda x: x["_merge"] == "right_only"]
            .drop("_merge", axis=1)
        )

    new_cases = (
        CaseData(
            date=row.Index.strftime("%Y-%m-%d"),
            cases=row.cases,
            deaths=row.deaths,
            recoveries=row.recoveries,
        )
        for row in df.itertuples()
    )

    save_cases(new_cases)
    dataframe_to_s3_csv(latest_data)

    return f"Update successful. {len(df.index)} row(s) updated."
