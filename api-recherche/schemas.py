from pydantic import BaseModel

class AircraftImageInfoBase(BaseModel):
    image_id: str
    width: float
    height: float
    type: str
    xmin_: float
    ymin_: float
    xmax_: float
    ymax_: float

class AircraftImageInfoCreate(AircraftImageInfoBase):
    pass

class AircraftImageInfo(AircraftImageInfoBase):
    id: int

    class Config:
        orm_mode = True