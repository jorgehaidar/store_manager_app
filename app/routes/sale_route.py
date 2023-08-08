from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.schema.sale_schema import SaleSchema
from app.repositories.sale_repository import SaleRepository
from app.services.sale_service import SaleService
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.schema.user_schema import UserSchema
from .. import oaut2

router = APIRouter(
    prefix='/sales',
    tags=['sales']
)


@router.get("/")
async def read_sales(db: Session = Depends(get_db),
                     current_user: UserSchema = Depends(oaut2.get_current_user)):
    sale_repository = SaleRepository(db)
    sale_service = SaleService(sale_repository)
    return await sale_service.get_sales()


@router.get("/{sale_id}")
async def read_sale(sale_id: int,
                    db: Session = Depends(get_db),
                    current_user: UserSchema = Depends(oaut2.get_current_user)):
    sale_repository = SaleRepository(db)
    sale_service = SaleService(sale_repository)
    sale = sale_service.get_sale_by_id(sale_id=sale_id)
    if sale is None:
        raise HTTPException(
            status_code=404,
            detail='Sale not found'
        )
    return sale

#TODO: El estado de respuesta de creado debe ser 201
@router.post("/")
async def create_sale(sale: SaleSchema,
                      db: Session = Depends(get_db),
                      current_user: UserSchema = Depends(oaut2.get_current_user)):
    sale_repository = SaleRepository(db)
    sale_service = SaleService(sale_repository)
    return sale_service.create_sale(sale=sale)


@router.put("/{sale_id}")
async def update_sale(sale_id: int,
                      sale: SaleSchema,
                      db: Session = Depends(get_db),
                      current_user: UserSchema = Depends(oaut2.get_current_user)):
    sale_repository = SaleRepository(db)
    sale_service = SaleService(sale_repository)
    return sale_service.update_sale(sale_id=sale_id, sale=sale)


@router.delete("/{sale_id}")
async def delete_sale(sale_id: int,
                      db: Session = Depends(get_db),
                      current_user: UserSchema = Depends(oaut2.get_current_user)):
    sale_repository = SaleRepository(db)
    sale_service = SaleService(sale_repository)
    sale_service.delete_sale(sale_id=sale_id)
    return {"message": "Client deleted successfully."}
