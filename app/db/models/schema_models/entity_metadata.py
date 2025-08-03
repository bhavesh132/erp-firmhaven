# app/db/models/schema_models/entity_metadata.py

from sqlalchemy import Column, String, Text, TIMESTAMP, ForeignKey, Boolean, JSON, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from app.db.base import Base

class EntityDefinition(Base):
    __tablename__ = "entity_definitions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    label = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    fields = relationship("FieldDefinition", back_populates="entity")


class FieldDefinition(Base):
    __tablename__ = "field_definitions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    entity_id = Column(UUID(as_uuid=True), ForeignKey("entity_definitions.id"))
    name = Column(String, nullable=False)
    label = Column(String, nullable=False)
    type = Column(String, nullable=False)
    enum_values = Column(JSON, nullable=True)
    fk_entity_name = Column(String, nullable=True)
    is_nullable = Column(Boolean, default=True)
    is_computed = Column(Boolean, default=False)
    computed_formula = Column(Text, nullable=True)
    default_value = Column(Text, nullable=True)
    rbac_config = Column(JSON, nullable=True)

    entity = relationship("EntityDefinition", back_populates="fields")
