import uvicorn
from fastapi import FastAPI
from app.db.database import Base, engine, SessionLocal
from app.routes import item_route

from app.models.item import Item
from app.schema.item_schema import ItemSchema

app = FastAPI()
app.include_router(item_route.router)
# TODO: add client api routes
# TODO: add sale api routes

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
    #Base.metadata.drop_all(engine)
    #Base.metadata.create_all(engine)

