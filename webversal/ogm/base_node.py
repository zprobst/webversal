
from pydantic import BaseModel


class BaseNode(BaseModel):
    @classmethod
    def node_label(cls):
        return cls.__name__


    def save(self):
        pass

    def refresh(self):
        pass

    

