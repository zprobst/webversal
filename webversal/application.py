from typing import Type


from .config import FrameworkConfiguration
from .servers import WebServer


class Application:
    configuration_class: Type[FrameworkConfiguration]

    def __init__(self) -> None:
        self.configuration = self.configuration_class.load()

    def serve_traffic(self) -> WebServer:
        return self.configuration.load_web_app_and_serve()
