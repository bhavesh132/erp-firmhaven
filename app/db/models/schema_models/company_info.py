from sqlalchemy import Column, Integer, String, DateTime, Boolean, JSON, func
from datetime import datetime
from app.db.base import Base

class CompanyInfo(Base):
    __tablename__ = "company_info"

    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    schema_name = Column(String, nullable=False, unique=True)
    slug = Column(String, nullable=False, unique=True)
    logo_url = Column(String)
    admin_email = Column(String)
    support_email = Column(String)
    sso_enabled = Column(Boolean, default=False)
    subscription = Column(JSON)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())