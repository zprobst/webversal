from starlette.types import ASGIApp
from pydantic import BaseSettings

from .web_server import WebServer

class WebServerConfiguration(BaseSettings):
    server: str = "uvicorn"
    base_path: str = "/"

    def wrap_app_with_web_server(self, app: ASGIApp) -> WebServer:
        server = WebServer.get_by_server_name(self.server, app)
        server.prepare_server(self)
        return server
