from pydantic import BaseModel


# payloads structure

class AddCar(BaseModel):
    name: str
    plate: str
    vin: str
    distance: int
    cid: str
    data: dict


class LoadCar(BaseModel):
    automotive_id: str


class SaveEditedCar(BaseModel):
    name: str
    plate: str
    vin: str
    distance: int
    cid: str
    data: dict
