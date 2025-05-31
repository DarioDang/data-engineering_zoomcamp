FROM python:3.12.4

RUN apt-get install wget
RUN pip install pandas==2.2.0 sqlalchemy psycopg2-binary pyarrow

WORKDIR /app
COPY ingest_data.py ingest_data.py 

ENTRYPOINT ["python", "ingest_data.py"]