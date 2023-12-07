from sqlalchemy import Column, Integer, Float, String
import database as db

class AircraftImageInfo(db.Base):
    __tablename__ = "aircraft_image_info"

    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(String)
    width = Column(Float)
    height = Column(Float)
    type = Column(String)
    xmin_ = Column(Float)
    ymin_ = Column(Float)
    xmax_ = Column(Float)
    ymax_ = Column(Float)