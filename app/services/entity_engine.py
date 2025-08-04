# services/entity_engine.py

from app.db.models.schema_models import entity_metadata
from app.utils.sql_generator import generate_create_table_sql
from uuid import uuid4
from app.schemas.entity import EntityCreate
from sqlalchemy import text

def create_entity(schema_name: str, entity_data: EntityCreate, db):
    EntityDefinition, FieldDefinition = entity_metadata.EntityDefinition, entity_metadata.FieldDefinition

    # 1. Validate entity name uniqueness
    existing = db.query(EntityDefinition).filter_by(name=entity_data.name).first()
    if existing:
        print(existing)
        raise ValueError(f"Entity '{entity_data.name}' already exists.")

    # 2. Insert entity_definitions
    entity = EntityDefinition(
        id=uuid4(),
        name=entity_data.name,
        label=entity_data.label,
        description=entity_data.description
    )
    db.add(entity)
    db.flush()  # to get entity.id

    # 3. Insert field_definitions
    for f in entity_data.fields:
        field = FieldDefinition(
            id=uuid4(),
            entity_id=entity.id,
            name=f.name,
            label=f.label,
            type=f.type,
            enum_values=f.enum_values,
            fk_entity_name=f.fk_entity_name,
            is_nullable=f.is_nullable,
            is_computed=f.is_computed,
            computed_formula=f.computed_formula,
            default_value=f.default_value,
            rbac_config=f.rbac_config
        )
        db.add(field)

    # 4. Commit definitions
    db.commit()

    # 5. Generate CREATE TABLE SQL and run it
    create_sql = generate_create_table_sql(schema_name, entity_data)
    db.execute(text(create_sql))
    db.commit()

    return {"status": "success"}
