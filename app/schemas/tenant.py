from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class SubscriptionCreate(BaseModel):
    plan_name: str
    seats: int
    status: str
    plan_metadata: dict = {}

class TenantCreate(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "Acme Corp"})
    schema_name: str = Field(..., json_schema_extra={"example": "acme_corp"})
    external_tenant_id: Optional[str] = Field(None, json_schema_extra={"example": "12345678-abcd"})
    slug: Optional[str] = Field(None, json_schema_extra={"example": "acme"})

    admin_email: Optional[EmailStr] = None
    support_email: Optional[EmailStr] = None
    logo_url: Optional[str] = None

    sso_enabled: Optional[bool] = False
    sso_metadata_url: Optional[str] = None
    sso_entity_id: Optional[str] = None

    subscription: SubscriptionCreate

class TenantRead(BaseModel):
    id: int
    name: str
    schema_name: str
    slug: Optional[str]
    admin_email: Optional[EmailStr]

    class Config:
        orm_mode = True
