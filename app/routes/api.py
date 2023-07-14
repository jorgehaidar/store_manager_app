import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.providers.clientService import ClientService
from app.providers.itemService import ItemService
from app.providers.salesService import SalesService
from app.models.item import Item
from app.models.client import Client
from app.models.sales import Sales

from typing import Any


app = FastAPI()


@app.get('/')
async def test():
    return {'hello': 'World'}


#Routers Item
#index, store, update, delete
@app.get('/item/index')
async def item_index():
    return ItemService.index()

@app.post('/item/store/')
async def item_store(model_item: Item):
    item_service = ItemService()
    return item_service.store(model_item)
    #return ItemService.store(model_item)

@app.get('/item/show/{id}')
async def item_show(id: int):
    return ItemService.show()

@app.put('/item/update')
def item_update(item_data: Item):
    return ItemService.update()

@app.delete('/item/delete/{id}')
def item_delete(id: int):
    return ItemService.delete()


#Routers Client

@app.get('/client/index')
def client_index():
    return ClientService.index(Client)

@app.post('/client/store/')
def client_store(model_client: Client):
    return 'hola'
    #return ClientService.store()

@app.get('/client/show/{id}')
def client_show(id: int):
    return ClientService.show()

@app.put('/client/update')
def client_update(client_data: Client):
    return ClientService.update()

@app.delete('/client/delete/{id}')
def client_delete(id: int):
    return ClientService.delete()


#Routers Sales

@app.get('/sales/index')
def sales_index():
    return SalesService.index(Sales)

@app.post('/sales/store/')
def sales_store(model_sales: Sales):
    return 'hola'
    #return SalesService.store()

@app.get('/sales/show/{id}')
def sales_show(id: int):
    return SalesService.show()

@app.put('/sales/update')
def sales_update(sales_data: Sales):
    return SalesService.update()

@app.delete('/client/delete/{id}')
def sales_delete(id: int):
    return SalesService.delete()

