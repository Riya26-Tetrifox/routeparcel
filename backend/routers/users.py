from fastapi import APIRouter,Depends,File,UploadFile
from sqlalchemy.orm import Session
from backend.deps import get_db
from backend.models import Customer
import xml.etree.ElementTree as ET
from backend.logging import logger
router=APIRouter()

@router.post("/uploadfile/")
async def upload_xml(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # ... means ellipse file can  be empty
    content = await file.read()
#  as the file is not in normal text so read it 
    root = ET.fromstring(content)
    # "Convert XML text into a tree structure that Python can understand."
    parcels = root.find("parcels")
    if parcels is None:
        return {"error": "No parcels found in XML"}
    parcels_data = []
    for parcel in root.find("parcels").findall("Parcel"):

        name = parcel.find("Receipient/Name").text
        street = parcel.find("Receipient/Address/Street").text
        house = parcel.find("Receipient/Address/HouseNumber").text
        postcode = parcel.find("Receipient/Address/PostalCode").text
        city = parcel.find("Receipient/Address/City").text
        weight = parcel.find("Weight").text
        value = parcel.find("Value").text
   
        existing = db.query(Customer).filter(
            Customer.Name == name,
            Customer.Street == street,
            Customer.City == city
        ).first()
        if not existing:
            user_id = Customer(
                Name=name,
                Street=street,
                HouseNumber=house,
                PostCode=postcode,
                City=city,
                Weight=weight,
                Value=value
            )
            db.add(user_id)
    db.commit()
    logger.info("Parcels uploaded successfully")
    return {"message": " parcels saved successfully"} 
