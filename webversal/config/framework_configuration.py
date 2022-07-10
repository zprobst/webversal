from pydantic import BaseSettings


from ..ogm import DatabaseConfiguration
from ..logging import LoggingConfiguration
from ..servers import WebServerConfiguration, WebServer


class FrameworkConfiguration(BaseSettings):
    server: WebServerConfiguration
    logging: LoggingConfiguration
    database: DatabaseConfiguration

    @classmethod
    def load(cls, env_name: str):
        dot_env_file = f"{env_name}.env"
        return cls(_env_file=dot_env_file)

    def load_web_app_and_serve(self) -> WebServer:
        ...