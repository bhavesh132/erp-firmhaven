from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Subscription(Base):
    __tablename__ = "subscriptions"
    __tableargs__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey("public.tenants.id", ondelete="CASCADE"), nullable=False)
    plan_name = Column(String, nullable=False)
    seats = Column(Integer, nullable=False)
    plan_metadata  = Column(JSON, default={})
    status = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    tenant = relationship("Tenant", back_populates="subscription")