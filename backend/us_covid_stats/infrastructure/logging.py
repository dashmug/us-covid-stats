import json
import logging
from functools import wraps
from typing import Any, Callable, Mapping

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log_event(func: Callable[[Any, Any], Any]) -> Callable[[Any, Any], Any]:
    @wraps(func)
    def wrapper(event: Any, context: Any) -> Any:
        logger.info(json.dumps(event))

        return func(event, context)

    return wrapper
