from abc import ABC, abstractmethod

from pydantic import BaseModel

class ActiveDatabaseObject(BaseModel, ABC):
    """Stores Common behvior between BaseNode and BaseRelationship. 
    
    Both objects share common logic for saving and refreshing that data from 
    the database as well as others. What varies in minor differences as well as
    the underlying queries used during the operations.
    """

    # TODO: How to store confg? 

    def save(self):
        pass

    def refresh(self):
        pass

    def delete(self):
        pass

    @abstractmethod
    def get_query_variables(self):
        ...