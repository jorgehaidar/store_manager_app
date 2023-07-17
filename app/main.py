import json

from app.db.database import Base, engine, SessionLocal
from app.routes.api import app
import uvicorn

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
    #Base.metadata.drop_all(engine)
    #Base.metadata.create_all(engine)
