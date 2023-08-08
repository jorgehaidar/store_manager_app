import uvicorn
from fastapi import FastAPI
from app.routes import item_route, client_route, sale_route, user_route, authentication

app = FastAPI()
app.include_router(authentication.router)
app.include_router(item_route.router)
app.include_router(client_route.router)
app.include_router(sale_route.router)
app.include_router(user_route.router)


if __name__ == '__main__':
    # To Run
    uvicorn.run('main:app', reload=True)

    # To DEBUG
    # uvicorn.run(app, host='127.0.0.1', port=8081)

    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)

