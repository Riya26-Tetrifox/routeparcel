from pydantic import BaseModel
class ShowCustomer(BaseModel):
    Id:int
    Name:str
    Street:str
    HouseNumber:int
    PostCode:str
    City:str
    Weight:float
    Value:float
    Department:str|None=None
    Insurance:str|None=None
    Approval_status:str|None=None

    class Config():
        orm_mode = True

