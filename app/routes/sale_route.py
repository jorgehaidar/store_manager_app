from typing import List

from fastapi import APIRouter, Depends
from app.schema.sale_schema import SaleSchema
from app.repositories.sale_repository import SaleRepository
from app.services.sale_service import SaleService

router = APIRouter()


@router.get("/sales")
async def read_sales(sale_repository: SaleRepository = Depends()):
    return await sale_repository.get_sales()


@router.get("/sales/{sale_id}", response_model=SaleSchema)
async def read_sale(sale_id: int, sale_repository: SaleRepository = Depends()):
    return sale_repository.get_sale_by_id(sale_id=sale_id)


@router.post("/sales", response_model=SaleSchema)
async def create_sale(sale: SaleSchema, sale_repository: SaleRepository = Depends()):
    return sale_repository.create_sale(sale=sale)


@router.put("/sales/{sale_id}", response_model=SaleSchema)
async def update_sale(sale_id: int, sale: SaleSchema, sale_repository: SaleRepository = Depends()):
    return sale_repository.update_sale(sale_id=sale_id, sale=sale)


@router.delete("/sales/{sale_id}")
async def delete_sale(sale_id: int, sale_repository: SaleRepository = Depends()):
    sale_repository.delete_sale(sale_id=sale_id)
    return {"message": "Client deleted successfully."}
