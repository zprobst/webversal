from webversal.tricks.case_conversions import camel_to_snake_case


from .active_datbase_object import ActiveDatabaseObject


GET_BY_ID_QUERY = """
MATCH ()-[r]-()
WHERE id(r) = $id
RETURN r
"""

CREATE_QUERY = """ 
CREATE (n:)
"""

CREATE_UNIQUE_QUERY = """ 
"""


class BaseNode(ActiveDatabaseObject):
    @classmethod
    def relationship_type(cls):
        return camel_to_snake_case(cls.__name__, lower=False)


