from logging import Logger
from typing import Optional

from .configuration import LoggingConfiguration
from .context import ContextInitMiddleware, add_context_var
from .correlation_id_middleware import CorrelationIdMiddleware
from .mixin import LoggerMixin
from .request_summary_middleware import RequestSummaryMiddleware

_logging_config: Optional[LoggingConfiguration] = None


def get_logger(name: str) -> Logger:
    if _logging_config is None:
        raise ValueError(
            f"Tried to get logger of name '{name}' before logging was initialized"
        )

    return _logging_config.get_logger(name)


def set_config(configuration: LoggingConfiguration) -> None:
    global _logging_config

    _logging_config = configuration


__all__ = (
    "get_logger",
    "LoggerMixin",
    "set_config",
    "LoggingConfiguration",
    "add_context_var",
    "ContextInitMiddleware",
    "CorrelationIdMiddleware",
    "RequestSummaryMiddleware",
)
