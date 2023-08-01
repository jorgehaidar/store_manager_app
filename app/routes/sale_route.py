from typing import List

from fastapi import APIRouter, Depends
from app.schema.sale_schema import SaleSchema
from app.repositories.sale_repository import SaleRepository
from app.services.sale_service import SaleService
from app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/sales")
async def read_sales(db: Session = Depends(get_db)):
    sale_repository = SaleRepository(db)
    sale_service = SaleService(sale_repository)
    return await sale_service.get_sales()


@router.get("/sales/{sale_id}")
async def read_sale(sale_id: int, db: Session = Depends(get_db)):
    sale_repository = SaleRepository(db)
    sale_service = SaleService(sale_repository)
    return sale_service.get_sale_by_id(sale_id=sale_id)


@router.post("/sales")
async def create_sale(sale: SaleSchema, db: Session = Depends(get_db)):
    sale_repository = SaleRepository(db)
    sale_service = SaleService(sale_repository)
    return sale_service.create_sale(sale=sale)


@router.put("/sales/{sale_id}")
async def update_sale(sale_id: int, sale: SaleSchema, db: Session = Depends(get_db)):
    sale_repository = SaleRepository(db)
    sale_service = SaleService(sale_repository)
    return sale_service.update_sale(sale_id=sale_id, sale=sale)


@router.delete("/sales/{sale_id}")
async def delete_sale(sale_id: int, sale_repository: SaleRepository = Depends()):
    sale_repository.delete_sale(sale_id=sale_id)
    return {"message": "Client deleted successfully."}
