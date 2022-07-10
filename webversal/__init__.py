from typing import Type

import uvloop

from .application import Application


def serve_traffic(cls: Type[Application] = Application, use_uv_loop=True):
    if use_uv_loop:
        uvloop.install()

    cls().serve_traffic()
