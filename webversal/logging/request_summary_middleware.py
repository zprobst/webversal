from starlette.middleware.base import (
    BaseHTTPMiddleware,
    Request,
    RequestResponseEndpoint,
    Response,
)

from .mixin import LoggerMixin


class RequestSummaryMiddleware(BaseHTTPMiddleware, LoggerMixin):
    def log_request_summary(self, request: Request):
        self.logger.info(
            "Recieved request", extra={"url": request.url, "method": request.method}
        )

    def log_response_summary(self, response: Response):
        self.logger.info(
            "Sending Response",
            extra={
                "status_code": response.status_code,
                "content-length": len(response.body),
            },
        )

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        self.log_request_summary(request)
        response = await call_next(request)
        self.log_response_summary(response)
        return response


# ORDER:
# ContextInitMiddleware
# CorrelationIdMiddleware
# RequestSummaryMiddleware
