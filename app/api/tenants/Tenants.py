from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.tenant import TenantCreate
from app.services.tenant_service import create_tenant
from app.db.session import get_db

router = APIRouter()

@router.post("/tenants")
def create_tenant_route(data: TenantCreate, db: Session = Depends(get_db)):
    try: 
        tenant = create_tenant(db, data)
        return {"id": tenant.id, "schema": tenant.schema_name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))