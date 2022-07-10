from functools import cache, cached_property
from logging import Logger, getLogger
from typing import Optional

from pydantic import BaseModel
from pythonjsonlogger.jsonlogger import JsonFormatter

from .context import logging_context


class ContextAwareJsonFormatter(JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        context_fields = logging_context.get({})
        log_record.update(context_fields)


def make_handler_for_color_formatting(format: str):
    from colorlog import ColoredFormatter, StreamHandler

    handler = StreamHandler()
    handler.setFormatter(ColoredFormatter(format))
    return handler


def make_handler_for_json_formatting(format: str):
    from logging import StreamHandler

    handler = StreamHandler()
    handler.setFormatter(ContextAwareJsonFormatter(format))
    return handler


FORMATTER_STRING_TO_HANDLER_FACTORY_MAP = {
    "json": make_handler_for_json_formatting,
    "color": make_handler_for_color_formatting,
}


class LoggingConfiguration(BaseModel):
    formatter: str = "json"
    format: str = "%(asctime)s %(name)s %(message)s %(levelname)s"
    correlation_header: Optional[str] = "X-Request-Id"

    @cached_property
    def handler(self):
        handler_factory = FORMATTER_STRING_TO_HANDLER_FACTORY_MAP[self.formatter]
        return handler_factory(self.format)

    @cache
    def get_logger(self, name: str) -> Logger:
        logger = getLogger(name)
        logger.addHandler(self.handler)
        return logger
