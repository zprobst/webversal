from abc import ABC, abstractmethod
from typing import Any, Dict, Type

from starlette.types import ASGIApp

from .web_server_configuration import WebServerConfiguration

_web_server_name_registry: Dict[str, Type["WebServer"]] = {}


class WebServer(ABC):
    def __init__(self, application: ASGIApp):
        self.application = application

    @abstractmethod
    def prepare_server(self, configuration: WebServerConfiguration):
        ...

    @abstractmethod
    def run_server(self) -> Any:
        ...

    def __init_subclass__(cls, name=None) -> None:
        _web_server_name_registry[name] = cls

    @classmethod
    def get_by_server_name(
        cls, server_name: str, application: ASGIApp
    ) -> "WebServer":
        return _web_server_name_registry[server_name](application)
