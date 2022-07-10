import importlib
from http import server

__all__ = []


def attempt_to_import_web_server_integration(module: str, server_class_name: str):
    try:
        module = importlib.import_module(module, __package__)
        __all__.append(getattr(module, server_class_name))
    except ImportError:
        pass


attempt_to_import_web_server_integration("hypercorn", "HypercornWebServer")
attempt_to_import_web_server_integration("mangum", "MangumWebServer")
attempt_to_import_web_server_integration("uvicorn", "UvicornWebServer")
