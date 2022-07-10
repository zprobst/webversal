from typing import Optional

from ..logging import LoggerMixin
from .abc import Task, TaskBackend, R


_current_backend: Optional[TaskBackend] = None


class BaseTask(Task, LoggerMixin):
    async def enqueue(self, require_result: bool = False) -> R:
        if _current_backend is None:
            self.logger.warning(
                "Running async job in process because a tasks backend was not defined"
            )
            return await self.perform()

        return await _current_backend.enqueue(self, require_result=require_result)


class BaseTaskBackend(TaskBackend, LoggerMixin):
    pass
