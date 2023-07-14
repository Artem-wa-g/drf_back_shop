FROM python:3.11
RUN mkdir /drf_back_shop

WORKDIR /drf_back_shop

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

#WORKDIR /src
#
#CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000