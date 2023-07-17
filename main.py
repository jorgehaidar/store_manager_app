import uvicorn
from fastapi import FastAPI
from app.db.database import Base, engine, SessionLocal
from app.routes import items
from app.db.item_db import Item

app = FastAPI()
app.include_router(items.router)


session = SessionLocal()


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
    #Base.metadata.drop_all(engine)
    #Base.metadata.create_all(engine)

