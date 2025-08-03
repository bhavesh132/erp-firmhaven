from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from app.db.base import Base
from sqlalchemy.orm import relationship

class Tenant(Base):
    __tablename__ = "tenants"
    __table_args__ = {"schema": "public"}  

    id = Column(Integer, primary_key=True)
    external_tenant_id = Column(String, unique=True, nullable=True)
    name = Column(String, nullable=False, unique=True)
    schema_name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now())
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    sso_enabled = Column(Boolean, default=False)
    sso_metadata_url = Column(String, nullable=True)
    sso_entity_id = Column(String, nullable=True)
    admin_email = Column(String, nullable=True)
    support_email = Column(String, nullable=True)
    logo_url = Column(String, nullable=True)
    slug = Column(String, unique=True, nullable=True)

    roles = relationship("Role", back_populates="tenant", cascade="all, delete-orphan")
    subscription = relationship("Subscription", back_populates="tenant", uselist=False)

