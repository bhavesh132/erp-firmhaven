from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.db.base import Base, import_base_models
from app.db.models.tenant import Tenant
from app.db.models.subscriptions import Subscription
from app.db.models.schema_models.company_info import CompanyInfo
from datetime import datetime


def create_base_tables_for_tenant(db: Session, schema_name: str, tenant_id: int, db_url: str) -> None:
    """
    Create all base tables (users, permissions, logs, etc.) in the new schema.
    Also insert initial company_info from public schema.
    """

    # 1. Fetch public schema data
    tenant: Tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    subscription: Subscription = db.query(Subscription).filter(Subscription.tenant_id == tenant_id).first()

    print(tenant, subscription)
    if not tenant or not subscription:
        raise ValueError("Tenant or Subscription not found")

    # 2. Create a schema-scoped engine using search_path
    tenant_engine = create_engine(
        db_url,
        connect_args={"options": f"-csearch_path={schema_name}"},
        pool_pre_ping=True
    )

    import_base_models()
    # 3. Create all base models in the tenant schema
    Base.metadata.create_all(bind=tenant_engine)

    # 4. Insert company_info
    with Session(tenant_engine) as tenant_db:
        info = CompanyInfo(
            tenant_id=str(tenant.id),
            name=tenant.name,
            schema_name=schema_name,
            slug=tenant.slug,
            logo_url=tenant.logo_url,
            admin_email=tenant.admin_email,
            support_email=tenant.support_email,
            sso_enabled=tenant.sso_enabled,
            subscription={
                "plan_name": subscription.plan_name,
                "seats": subscription.seats,
                "status": subscription.status,
                "plan_metadata": subscription.plan_metadata,
            },
        )
        tenant_db.add(info)
        tenant_db.commit()
