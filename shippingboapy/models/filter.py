from pydantic import BaseModel
from enum import Enum
from typing import ClassVar, Any
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
    value: Any
    _ARRAY_FIELDS: ClassVar[list[str]] = ["updated_at", "created_at", "shipped_at", "delivered_at", "reason"]
    _JOIN_FIELDS: ClassVar[dict[str, str]] = {}  # vide par défaut : pas de jointure

    def to_params(self) -> str:
        key = f"[{self.field}__{self.operator.value}]"
        if self.field in self._JOIN_FIELDS:
            key = f"[joins][{self._JOIN_FIELDS[self.field]}]{key}"
        if self.field in self._ARRAY_FIELDS:
            key = f"{key}[]"
        return key

class ProductVariationStockFilter(Filter):
    _JOIN_FIELDS: ClassVar[dict[str, str]] = {"ean13": "product", "title": "product", "user_ref": "product"}