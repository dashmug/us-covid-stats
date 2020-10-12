import json
import logging
from functools import wraps
from typing import Any, Callable, Mapping

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log_event(
    func: Callable[[Mapping[str, Any], Any], Any]
) -> Callable[[Mapping[str, Any], Any], Any]:
    @wraps(func)
    def wrapper(event: Mapping[str, Any], context: Any) -> Any:
        logger.info(json.dumps(event))

        return func(event, context)

    return wrapper
