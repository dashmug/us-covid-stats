from typing import Any

import boto3
from us_covid_stats.config.settings import FRONTEND_URL, NOTIFICATION_TOPIC

sns = boto3.resource("sns")
topic = sns.Topic(NOTIFICATION_TOPIC)


def notify(message: str, condition: str) -> Any:
    return topic.publish(
        Message=" ".join([message, f"View dashboard at {FRONTEND_URL}."]),
        Subject="Data refresh successful.",
        MessageAttributes={
            "condition": {
                "DataType": "String",
                "StringValue": condition,
            }
        },
    )
