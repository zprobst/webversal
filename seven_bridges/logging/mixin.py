from seven_bridges.tricks.class_property import classproperty

from . import get_logger


class LoggerMixin:
    @classproperty
    def logger(cls):
        return get_logger(cls.__name__)
