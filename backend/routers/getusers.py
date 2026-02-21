from fastapi import APIRouter,Depends,HTTPException
from typing import List
from backend.schemas import ShowCustomer
from sqlalchemy.orm import Session
from backend.deps import get_db
from backend.models import Customer
from backend.logging import logger
router=APIRouter()

@router.get("/responsefile",response_model=List[ShowCustomer])
def get_user(db:Session=Depends(get_db)):
    return db.query(Customer).all()  
@router.post("/apply-insurance/{customer_id}")
def apply_single_insurance(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.Id == customer_id).first()
    if not customer:
        logger.error("Customer not found")
        raise HTTPException(status_code=404, detail="Customer not found")
    customer.Insurance = "Completed"
    customer.Approval_status = "Approved"
    db.commit()
    db.refresh(customer)
    logger.info(f"Insurance applied for customer {customer_id}")
    return customer