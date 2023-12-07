import requests
import os
from PIL import Image
from fastapi import Depends, FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import service, models, schemas
import database as db
from sqlalchemy.orm import Session

URL_AIRCRAFTDETECT = "http://api-aircraftdetect:8000/"

app = FastAPI()

def get_db():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

@app.post("/image")
async def post_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        request_image_name = 'images/' + file.filename
        with open(request_image_name, 'wb') as request_image:
            request_image.write(file.file.read())
        
        width, height = transform_image(request_image_name, 'result_img.jpg')

        with open('result_img.jpg', 'rb') as result_img:
            response = requests.post(URL_AIRCRAFTDETECT, files={"file": result_img})
        

        if response.status_code == 200:
            json_response = response.json()
            newInfos = []
            for json_item in json_response:
                newInfo = schemas.AircraftImageInfoCreate(
                    image_id = file.filename.split('.')[0],
                    width = width,
                    height = height,
                    type = json_item['name'],
                    xmin_ = json_item['xmin'],
                    ymin_ = json_item['ymin'],
                    xmax_ = json_item['xmax'],
                    ymax_ = json_item['ymax']
                )
                newInfos.append(newInfo)
            service.create_AircraftImageInfo(db=db, newInfos=newInfos)
            return JSONResponse(content=json_response)
        
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    finally:
        if os.path.exists('result_img.jpg'):
            os.remove('result_img.jpg')

@app.get("/image/{id}")
async def get_image(id):
    img_paths = 'images/' + id + '.jpg'
    return FileResponse(img_paths)

@app.get("/search")
async def get_all_info(db: Session = Depends(get_db)):
    return service.get_AircraftImageInfo(db=db)

@app.get("/search/type/{type}")
async def get_info_by_type(type, db: Session = Depends(get_db)):
    return service.get_AircraftImageInfo_by_type(db=db, type=type)

@app.get("/search/image_id/{image_id}")
async def get_info_by_image_id(image_id, db: Session = Depends(get_db)):
    return service.get_AircraftImageInfo_by_image_id(db=db, image_id=image_id)

def transform_image(input_path, output_path):
    original_image = Image.open(input_path, 'r')
    width, height = original_image.size
    square_image = Image.new("RGB", (width, width), (0, 0, 0))
    square_image.paste(original_image, (0, 0))

    square_image.save(output_path)
    return width, height