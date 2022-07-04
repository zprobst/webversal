from typing import Optional
from uuid import uuid4

from starlette.middleware.base import (
    ASGIApp,
    BaseHTTPMiddleware,
    DispatchFunction,
    Request,
    RequestResponseEndpoint,
    Response,
)

from .context import add_context_var


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        dispatch: Optional[DispatchFunction] = None,
        correlation_header_name: str = "X-Request-Id",
    ) -> None:
        super().__init__(app, dispatch)
        self.correlation_header_name = correlation_header_name

    def generate_new_correlation_id(self):
        return str(uuid4())

    def get_correlation_id(self, request: Request) -> str:
        return (
            request.headers.get(self.correlation_header_name)
            or self.generate_new_correlation_id()
        )

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        correlation_id = self.get_correlation_id(request)
        add_context_var("correlation_id", correlation_id)
        result = await call_next(request)
        result.headers[self.correlation_header_name] = correlation_id
        return result
