from sqlalchemy import Column,Integer,String,Float,UniqueConstraint
from backend.database import Base

class Customer(Base):
    __tablename__="customer"
    Id=Column(Integer,primary_key=True,index=True)
    Name=Column(String,index=True)
    Street=Column(String)
    HouseNumber=Column(Integer)
    PostCode=Column(String)
    City=Column(String)
    Weight=Column(Float)
    Value=Column(Float)
    Department=Column(String)
    Insurance=Column(String)
    Approval_status=Column(String)



