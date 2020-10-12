from pandas import DataFrame


def merge_cases_with_recoveries(cases: DataFrame, recoveries: DataFrame) -> DataFrame:
    return (
        cases.join(recoveries, how="inner")
        .fillna(0)
        .rename(columns={"Recovered": "recoveries"})
        .astype({"recoveries": "int32"})
    )
