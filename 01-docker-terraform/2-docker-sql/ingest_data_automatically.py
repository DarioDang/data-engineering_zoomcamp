import pandas as pd
import os
from sqlalchemy import create_engine
import argparse 
import pyarrow

def ingest_month(engine, table_name, url, schema, if_exists_option):
    parquet_name = 'output.parquet'
    os.system(f"wget {url} -O {parquet_name}")
    # Read the Parquet file
    df = pd.read_parquet(parquet_name)
    # For the first month, you may want to replace, then append subsequently
    df.head(n=0).to_sql(name=table_name, con=engine, schema=schema, if_exists=if_exists_option)
    df.to_sql(name=table_name, con=engine, schema=schema, if_exists='append')
    # Remove the temporary file if needed
    os.remove(parquet_name)

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    base_url = params.url  # e.g., "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-"
    
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    # Ensure the target schema exists
    with engine.connect() as conn:
        conn.execute("CREATE SCHEMA IF NOT EXISTS nyc_trip_taxi;")
    
    # Loop over months 01 to 12:
    for month in [f'{i:02d}' for i in range(1, 4)]:
        file_url = f"{base_url}{month}.parquet"
        print(f"Ingesting data for month: {month} from {file_url}")
        # For the first month, if_exists='replace', else 'append'
        if month == '01':
            ingestion_mode = 'replace'
        else:
            ingestion_mode = 'append'
        ingest_month(engine, table_name, file_url, 'nyc_trip_taxi', ingestion_mode)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest monthly data into PostgreSQL')
    parser.add_argument('--user', help='User name for PostgreSQL')
    parser.add_argument('--password', help='Password for PostgreSQL')
    parser.add_argument('--host', help='Host for PostgreSQL')
    parser.add_argument('--port', help='Port for PostgreSQL')
    parser.add_argument('--db', help='Database name for PostgreSQL')
    parser.add_argument('--table_name', help='Table name for PostgreSQL')
    parser.add_argument('--url', help='Base URL of the parquet file to ingest (without month and .parquet)')
    args = parser.parse_args()
    main(args)

# How to run
# python ingest_data_automatically.py \
#   --user=root \
#   --password=root \
#   --host=localhost \
#   --port=5433 \
#   --db=ny_taxi \
#   --table_name=green_taxi_data \
#   --url="https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-"




