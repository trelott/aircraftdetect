FROM python:3.10
RUN apt update
RUN apt install 
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
RUN pip install uvicorn psycopg2-binary python-multipart
EXPOSE 8000
CMD ["/bin/sh","-c","uvicorn main:app --host 0.0.0.0 --port 8000"]