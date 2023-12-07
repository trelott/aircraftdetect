#FROM ac0ed82278fb2c2
#ADD https://ultralytics.com/assets/Arial.ttf https://ultralytics.com/assets/Arial.Unicode.ttf /root/.config/Ultralytics/
#RUN /bin/sh -c apt update
#RUN /bin/sh -c TZ=Etc/UTC apt install -y tzdata
#RUN /bin/sh -c apt install --no-install-recommends -y python3-pip git zip curl htop libgl1-mesa-glx libglib2.0-0 libpython3-dev gnupg
#COPY requirements.txt .
#RUN /bin/sh -c python3 -m pip install --upgrade pip wheel
#RUN /bin/sh -c pip install --no-cache -r requirements.txt albumentations gsutil notebook     coremltools onnx onnx-simplifier onnxruntime 'openvino-dev>=2022.3'     --extra-index-url https://download.pytorch.org/whl/cpu
#RUN /bin/sh -c mkdir -p /usr/src/app # buildkit
#WORKDIR /usr/src/app
#RUN /bin/sh -c git clone https://github.com/ultralytics/yolov5 /usr/src/app
#RUN /bin/sh -c pip install ultralytics fastapi uvicorn python-multipart
#COPY best.onnx .
#COPY worker.py .
#CMD ["/bin/sh","-c","uvicorn worker:app --host 0.0.0.0 --port 8000"]

FROM python:3.10
ADD https://ultralytics.com/assets/Arial.ttf https://ultralytics.com/assets/Arial.Unicode.ttf /root/.config/Ultralytics/
RUN apt update
RUN TZ=Etc/UTC apt install -y tzdata
RUN apt install --no-install-recommends -y python3-pip git zip curl htop libgl1-mesa-glx libglib2.0-0 libpython3-dev gnupg
RUN python3 -m pip install --upgrade pip wheel
RUN mkdir -p /usr/src/app # buildkit
WORKDIR /usr/src/app
RUN git clone https://github.com/ultralytics/yolov5 /usr/src/app
RUN pip install --no-cache -r requirements.txt
RUN pip install ultralytics fastapi uvicorn python-multipart onnx onnxruntime
COPY best.onnx .
COPY worker.py .
EXPOSE 8000
CMD ["/bin/sh","-c","uvicorn worker:app --host 0.0.0.0 --port 8000"]