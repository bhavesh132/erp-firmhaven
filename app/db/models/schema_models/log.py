from sqlalchemy import Column, Integer, String, DateTime, Boolean, func, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.base import Base

class ConfigLog(Base):
    __tablename__ = "config_logs"
    id = Column(Integer, primary_key=True)
    actor_user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    action = Column(String, nullable=False)
    target_table = Column(String, nullable=False)
    target_id = Column(Integer, nullable=False)
    before = Column(JSON)
    after = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    action = Column(String, nullable=False)
    entity_name = Column(String, nullable=False)
    record_id = Column(Integer, nullable=False)
    before = Column(JSON)
    after = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())