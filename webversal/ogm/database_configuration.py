from contextlib import contextmanager
from functools import cached_property

from neo4j import GraphDatabase
from pydantic import BaseModel


class DatabaseConfiguration(BaseModel):
    hostname: str
    username: str
    password: str
    database_name: str = "neo4j"
    connection_scheme: str = "neo4j"

    connection_acquisition_timeout: float | int = 60.0
    connection_timeout: float | int = 30.0
    max_connection_lifetime: int = 3600
    max_connection_pool_size: int = 200
    max_connection_retry_time: int = 30

    configure_database_on_start: bool = True

    @property
    def connection_uri(self) -> str:
        return "f{self.connection_scheme}://{self.hostname}"

    @cached_property
    def database(self) -> GraphDatabase:
        return GraphDatabase(
            uri=self.connection_uri,
            auth=(self.username, self.password),
            connection_acquisition_timeout=self.connection_acquisition_timeout,
            connection_timeout=self.connection_timeout,
            max_connection_lifetime=self.max_connection_lifetime,
            max_connection_pool_size=self.max_connection_pool_size,
            max_connection_retry_time=self.max_connection_retry_time
        )

    @contextmanager
    def session(self):
        with self.database.session(database_name=self.database_name) as session:
            yield session
