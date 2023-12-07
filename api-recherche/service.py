from sqlalchemy.orm import Session
import models, schemas
from typing import List

def get_AircraftImageInfo(db: Session):
    return db.query(models.AircraftImageInfo).all()

def get_AircraftImageInfo_by_type(db: Session, type: str):
    return db.query(models.AircraftImageInfo).filter(models.AircraftImageInfo.type == type).all()

def get_AircraftImageInfo_by_image_id(db: Session, image_id: str):
    return db.query(models.AircraftImageInfo).filter(models.AircraftImageInfo.image_id == image_id).all()

def create_AircraftImageInfo(db: Session, newInfos: List[schemas.AircraftImageInfoCreate]):
    db_newInfos = []
    for newInfo in newInfos:
        db_newInfo = models.AircraftImageInfo(
            image_id = newInfo.image_id,
            width = newInfo.width,
            height = newInfo.height,
            type = newInfo.type,
            xmin_ = newInfo.xmin_,
            ymin_ = newInfo.ymin_,
            xmax_ = newInfo.xmax_,
            ymax_ = newInfo.ymax_
        )
        db.add(db_newInfo)
        db.commit()
        db.refresh(db_newInfo)
        db_newInfos.append(db_newInfo)
    return db_newInfos

