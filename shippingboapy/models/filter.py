from pydantic import BaseModel
from enum import Enum

class Operator(str, Enum):
    BLANK = "blank"
    EQUALS = "eq"
    DIFFERENT = "neq"
    CONTAINS = "contains"
    NOT_CONTAINS = "ncontains"
    START = "starts_with"
    END = "ends_with"
    AMONG = "in"
    EXCLUDES = "nin"
    EXISTS = "exists"
    LOWER = "lt"
    LOWER_OR_EQUALS = "lte"
    GREATER = "gt"
    GREATER_OR_EQUALS = "gte"

class Filter(BaseModel):
    field: str
    operator: Operator
    value: str
    _filter_array : list[str] = ["updated_at", "created_at", "shipped_at", "delivered_at"]

    def to_params(self) -> str:
        filter_str = f"[{self.field}__{self.operator}]"
        if self.field in self._filter_array:        
            filter_str = filter_str + "[]"
        return filter_str
    