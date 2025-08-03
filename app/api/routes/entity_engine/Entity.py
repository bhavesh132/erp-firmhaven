from fastapi import APIRouter, Depends, HTTPException
from app.schemas.entity import EntityCreate
from app.services.entity_engine import create_entity
from app.db.models.schema_models import entity_metadata
from app.db.dependencies import get_tenant_context

router = APIRouter()

# POST /entities
@router.post("/entities")
def create_entity_route(
    entity_data: EntityCreate,
    ctx = Depends(get_tenant_context)
):
    db = ctx["db"]
    schema_name = ctx["schema_name"]
    try:
        return create_entity(schema_name, entity_data, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# GET /entities
@router.get("/entities")
def list_entities(ctx = Depends(get_tenant_context)):
    db = ctx["db"]
    schema_name = ctx["schema_name"]

    EntityDefinition = entity_metadata.EntityDefinition
    entities = db.query(EntityDefinition).all()
    return [
        {
            "name": e.name,
            "label": e.label,
            "description": e.description,
            "created_at": e.created_at,
            "updated_at": e.updated_at
        } for e in entities
    ]


# GET /entities/{name}
@router.get("/entities/{name}")
def get_entity_details(name: str, ctx = Depends(get_tenant_context)):
    db = ctx["db"]
    schema_name = ctx["schema_name"]

    EntityDefinition, FieldDefinition = entity_metadata.EntityDefinition, entity_metadata.FieldDefinition
    entity = db.query(EntityDefinition).filter_by(name=name).first()

    if not entity:
        raise HTTPException(status_code=404, detail="Entity not found")

    fields = db.query(FieldDefinition).filter_by(entity_id=entity.id).all()
    return {
        "name": entity.name,
        "label": entity.label,
        "description": entity.description,
        "fields": [
            {
                "name": f.name,
                "label": f.label,
                "type": f.type,
                "is_nullable": f.is_nullable,
                "is_computed": f.is_computed,
                "default_value": f.default_value,
                "enum_values": f.enum_values,
                "fk_entity_name": f.fk_entity_name,
                "rbac_config": f.rbac_config
            }
            for f in fields
        ]
    }