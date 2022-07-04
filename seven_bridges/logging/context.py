from contextvars import ContextVar
from typing import Any, Dict

from starlette.middleware.base import (
    BaseHTTPMiddleware,
    Request,
    RequestResponseEndpoint,
    Response,
)

logging_context: ContextVar[Dict[str, Any]] = ContextVar("logging_context")


def add_context_var(key: str, value: Any):
    try:
        logging_context.get()[key] = value
    except LookupError:
        logging_context.set({key: value})


class ContextInitMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        logging_context_reset_token = logging_context.set({})
        response = await call_next(request)
        logging_context.reset(logging_context_reset_token)
        return response
