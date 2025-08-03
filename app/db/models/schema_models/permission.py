from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    scope_type = Column(String, nullable=False)
    scope_id = Column(Integer, nullable=False)
    entity_name = Column(String, nullable=False)
    column_name = Column(String, nullable=False)
    access_level = Column(String, nullable=False)