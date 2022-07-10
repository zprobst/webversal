from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from pydantic import BaseModel

T = TypeVar("T", bound="Task")
R = TypeVar("R")


class Task(ABC, BaseModel, Generic[R]):
    @abstractmethod
    async def perform(self) -> R:
        ...

    @abstractmethod
    async def enqueue(self, require_result: bool = False) -> R:
        ...


class TaskBackend(ABC):
    @abstractmethod
    async def enqueue(self, model: T, require_result: bool = False) -> R | None:
        ...
