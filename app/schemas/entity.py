# app/schemas/entity.py

from typing import List, Optional, Literal, Union
from pydantic import BaseModel, Field, field_validator, model_validator
from uuid import UUID
import re

SQL_IDENTIFIER_REGEX = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")

class FieldCreate(BaseModel):
    name: str
    label: str
    type: Literal["string", "integer", "float", "boolean", "date", "datetime", "enum", "fk", "json", "computed"]
    enum_values: Optional[List[str]] = None
    fk_entity_name: Optional[str] = None
    is_nullable: bool = True
    is_computed: bool = False
    computed_formula: Optional[str] = None
    default_value: Optional[Union[str, int, float, bool]] = None
    rbac_config: Optional[dict] = None

    @model_validator(mode="after")
    def validate_dependent_fields(self):
        if self.type == "enum" and not self.enum_values:
            raise ValueError("enum_values must be provided for enum fields.")
        if self.type == "fk" and not self.fk_entity_name:
            raise ValueError("fk_entity_name must be provided for foreign key fields.")
        if self.is_computed and not self.computed_formula:
            raise ValueError("computed_formula must be provided for computed fields.")
        return self

class EntityCreate(BaseModel):
    name: str
    label: str
    description: Optional[str] = None
    fields: List[FieldCreate]

    @field_validator("name")
    def validate_sql_identifier(cls, v):
        if not SQL_IDENTIFIER_REGEX.match(v):
            raise ValueError("Entity name must be a valid SQL identifier")
        return v
