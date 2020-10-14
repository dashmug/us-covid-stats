import pandas
import pytest
from us_covid_stats.etl.transform import merge_cases_with_recoveries

same_size = {
    "nyt": pandas.DataFrame(
        data={
            "date": ["2020-09-02", "2020-09-03", "2020-09-04", "2020-09-05"],
            "cases": [6121948, 6168342, 6220446, 6262700],
            "deaths": [185639, 186717, 187697, 188409],
        }
    ).set_index("date"),
    "hopkins": pandas.DataFrame(
        data={
            "Date": ["2020-09-02", "2020-09-03", "2020-09-04", "2020-09-05"],
            "Recovered": [2231757, 2266957, 2283454, 2302187],
        }
    ).set_index("Date"),
}

off_by_one_1 = {
    "nyt": pandas.DataFrame(
        data={
            "date": [
                "2020-09-01",
                "2020-09-02",
                "2020-09-03",
                "2020-09-04",
                "2020-09-05",
            ],
            "cases": [6089504, 6121948, 6168342, 6220446, 6262700],
            "deaths": [184563, 185639, 186717, 187697, 188409],
        }
    ).set_index("date"),
    "hopkins": pandas.DataFrame(
        data={
            "Date": ["2020-09-02", "2020-09-03", "2020-09-04", "2020-09-05"],
            "Recovered": [2231757, 2266957, 2283454, 2302187],
        }
    ).set_index("Date"),
}

off_by_one_2 = {
    "nyt": pandas.DataFrame(
        data={
            "date": [
                "2020-09-02",
                "2020-09-03",
                "2020-09-04",
                "2020-09-05",
                "2020-09-06",
            ],
            "cases": [6121948, 6168342, 6220446, 6262700, 6292699],
            "deaths": [185639, 186717, 187697, 188409, 188820],
        }
    ).set_index("date"),
    "hopkins": pandas.DataFrame(
        data={
            "Date": ["2020-09-02", "2020-09-03", "2020-09-04", "2020-09-05"],
            "Recovered": [2231757, 2266957, 2283454, 2302187],
        }
    ).set_index("Date"),
}


off_by_one_3 = {
    "nyt": pandas.DataFrame(
        data={
            "date": ["2020-09-02", "2020-09-03", "2020-09-04", "2020-09-05"],
            "cases": [6121948, 6168342, 6220446, 6262700],
            "deaths": [185639, 186717, 187697, 188409],
        }
    ).set_index("date"),
    "hopkins": pandas.DataFrame(
        data={
            "Date": [
                "2020-09-02",
                "2020-09-03",
                "2020-09-04",
                "2020-09-05",
                "2020-09-06",
            ],
            "Recovered": [2231757, 2266957, 2283454, 2302187, 2315995],
        }
    ).set_index("Date"),
}


@pytest.mark.parametrize(
    "cases, recoveries",
    [
        (same_size["nyt"], same_size["hopkins"]),
        (off_by_one_1["nyt"], off_by_one_1["hopkins"]),
        (off_by_one_2["nyt"], off_by_one_2["hopkins"]),
        (off_by_one_3["nyt"], off_by_one_3["hopkins"]),
    ],
)
def test_merge_cases_with_recoveries(cases, recoveries):
    transformed = merge_cases_with_recoveries(cases, recoveries)
    pandas.testing.assert_frame_equal(
        transformed,
        pandas.DataFrame(
            data={
                "date": ["2020-09-02", "2020-09-03", "2020-09-04", "2020-09-05"],
                "cases": [6121948, 6168342, 6220446, 6262700],
                "deaths": [185639, 186717, 187697, 188409],
                "recoveries": [2231757, 2266957, 2283454, 2302187],
            }
        ).set_index("date"),
    )
