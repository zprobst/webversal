from typing import Any

from mangum import Mangum

from ..web_server import WebServer
from ..web_server_configuration import WebServerConfiguration


class MangumWebServer(WebServer):
    def prepare_server(self, configuration: WebServerConfiguration):
        self.handler = Mangum(
            self.application, api_gateway_base_path=configuration.base_path
        )

    def run_server(self) -> Any:
        return self.handler
