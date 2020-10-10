from typing import Any, Iterable, List, Mapping, Optional

import boto3
from boto3.dynamodb.conditions import Key
from us_covid_stats.config.settings import AWS_REGION, DATA_TABLE
from us_covid_stats.infrastructure.logging import logger

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)

data_table = dynamodb.Table(DATA_TABLE)


def put_item(pk: str, sk: str, **kwargs: Any) -> None:
    data_table.put_item(
        Item={
            "pk": pk,
            "sk": sk,
            **kwargs,
        },
    )


def batch_put_item(items: Iterable[Mapping[str, Any]]) -> None:
    with data_table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)


def get_item(pk: str, sk: str) -> Optional[Mapping[str, Any]]:
    response = data_table.get_item(Key={"pk": pk, "sk": sk})
    item: Optional[Mapping[str, Any]] = response.get("Item")

    return item


def query_all(
    pk: str,
    exclusive_start_key: Optional[Mapping[str, str]] = None,
) -> List[Any]:
    try:
        response = data_table.query(
            KeyConditionExpression=Key("pk").eq(pk),
            **{"ExclusiveStartKey": exclusive_start_key} if exclusive_start_key else {},
        )
        result: List[Any] = response.get("Items", [])
        last_evaluated_key = response.get("LastEvaluatedKey")
        if last_evaluated_key:
            return result + query_all(pk, last_evaluated_key)
        if len(result):
            return result
        return []
    except Exception:
        logger.error("An unexpected error occurred.", exc_info=True)
        return []
