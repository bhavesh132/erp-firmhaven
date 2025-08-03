from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.models.tenant import Tenant
from app.schemas.tenant import TenantCreate
from app.db.models.roles import Role
from app.db.models.subscriptions import Subscription
from app.services.schema_bootstrap import create_base_tables_for_tenant
from dotenv import load_dotenv
import os
from slugify import slugify


load_dotenv(".env")

DATABASE_URL = os.getenv("DATABASE_URL_PYTHON")
if not DATABASE_URL:
    raise ValueError("Database URL is not defined")



def create_tenant(db: Session, data: TenantCreate) -> Tenant:
    slug_value = slugify(data.name)
    new_tenant = Tenant(
        name=data.name,
        slug=slug_value,
        schema_name=data.schema_name,
        external_tenant_id=data.external_tenant_id,
        admin_email=data.admin_email,
        support_email=data.support_email,
        logo_url=data.logo_url,
        sso_enabled=data.sso_enabled,
        sso_metadata_url=data.sso_metadata_url,
        sso_entity_id=data.sso_entity_id
    )
    db.add(new_tenant)
    db.flush()
    
    db.refresh(new_tenant)


    schema_sql = text(f'CREATE SCHEMA IF NOT EXISTS "{data.schema_name}"')
    db.execute(schema_sql)

    role = Role(
        name="Tenant Admin",
        tenant_id=new_tenant.id,
        is_default=True,

    )
    db.add(role)

    sub = Subscription(
        tenant_id=new_tenant.id,
        plan_name=data.subscription.plan_name,
        seats=data.subscription.seats,
        status= data.subscription.status,
        plan_metadata=data.subscription.plan_metadata,
    )
    db.add(sub)


    db.commit()

    create_base_tables_for_tenant(db, data.schema_name, new_tenant.id, db_url=DATABASE_URL) # type: ignore
    return new_tenant