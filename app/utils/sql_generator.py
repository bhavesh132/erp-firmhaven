
def generate_create_table_sql(schema_name: str, entity_data):
    table_name = entity_data.name
    columns = []

    for field in entity_data.fields:
        line = f'"{field.name}"'
        if field.is_computed:
            continue  # Computed fields are not stored
        elif field.type == "string":
            line += " TEXT"
        elif field.type == "integer":
            line += " INTEGER"
        elif field.type == "float":
            line += " FLOAT"
        elif field.type == "boolean":
            line += " BOOLEAN"
        elif field.type == "date":
            line += " DATE"
        elif field.type == "datetime":
            line += " TIMESTAMP"
        elif field.type == "json":
            line += " JSONB"
        elif field.type == "enum":
            line += " TEXT"
        elif field.type == "fk":
            line += " UUID"  
        if not field.is_nullable:
            line += " NOT NULL"
        columns.append(line)

    sql = f'CREATE TABLE "{schema_name}"."{table_name}" (\n    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),\n    ' + ',\n    '.join(columns) + '\n);'
    return sql
