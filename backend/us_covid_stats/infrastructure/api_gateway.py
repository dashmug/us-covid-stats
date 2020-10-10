from typing import Any, Mapping


def create_response(
    body: str,
    content_type: str,
    is_base64: bool = False,
    status_code: int = 200,
) -> Mapping[str, Any]:

    return {
        "body": body,
        "isBase64Encoded": is_base64,
        "statusCode": status_code,
        "headers": {"Content-Type": content_type},
    }
