from fastapi import Depends, Header
from app.db.session import get_tenant_session

def get_schema_from_header(x_tenant_id: str = Header(...)) -> str:
    return f"{x_tenant_id}"

def get_tenant_context(
    schema_name: str = Depends(get_schema_from_header)
):
    with get_tenant_session(schema_name) as db:
        return {"schema_name": schema_name, "db": db}
