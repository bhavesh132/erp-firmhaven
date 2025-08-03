from fastapi import FastAPI
from app.api.tenants import Tenants
from app.api.routes.entity_engine import Entity

app = FastAPI()

app.include_router(Tenants.router, prefix='/api', tags=["Tenants"])
app.include_router(Entity.router, prefix='/api', tags=["Entity Engine"])

@app.get("/health")
def health_check():
    return {
        "status": "OK"
    }