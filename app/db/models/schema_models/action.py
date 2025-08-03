from sqlalchemy import Column, Integer, String, DateTime, func, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class ActionDefinition(Base):
    __tablename__ = "action_definitions"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_at = Column(DateTime, onupdate=func.now())
    config = Column(JSON)
    entity_name = Column(String, nullable=False)