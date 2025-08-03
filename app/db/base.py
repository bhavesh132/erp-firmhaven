from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
)

Base = declarative_base(metadata=metadata)

def import_models():
    from app.db.models.tenant import Tenant
    from app.db.models.roles import Role
    from app.db.models.subscriptions import Subscription

def import_base_models():
    from app.db.models.schema_models.company_info import CompanyInfo
    from app.db.models.schema_models.user import User
    from app.db.models.schema_models.group import Group
    from app.db.models.schema_models.permission import Permission
    from app.db.models.schema_models.log import ConfigLog, AuditLog
    from app.db.models.schema_models.action import ActionDefinition
    from app.db.models.schema_models.flow import FlowDefinition
    from app.db.models.schema_models.custom_view import CustomView
    from app.db.models.schema_models.entity_metadata import EntityDefinition, FieldDefinition
