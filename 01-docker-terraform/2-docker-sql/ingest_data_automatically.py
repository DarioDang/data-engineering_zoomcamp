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
    color = params.color.lower()
    year = params.year
    table_name = f"{color}_taxi_data"
    base_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{color}_tripdata_{year}-"

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    with engine.connect() as conn:
        conn.execute("CREATE SCHEMA IF NOT EXISTS nyc_trip_taxi;")
        conn.execute("CREATE SCHEMA IF NOT EXISTS dbt_production;")
    
    for month in [f'{i:02d}' for i in range(1, 4)]:
        file_url = f"{base_url}{month}.parquet"
        print(f"Ingesting data for month: {month} from {file_url}")
        ingestion_mode = 'replace' if month == '01' else 'append'
        ingest_month(engine, table_name, file_url, 'nyc_trip_taxi', ingestion_mode)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest NYC Taxi data into PostgreSQL')
    parser.add_argument('--user', help='User name for PostgreSQL')
    parser.add_argument('--password', help='Password for PostgreSQL')
    parser.add_argument('--host', help='Host for PostgreSQL')
    parser.add_argument('--port', help='Port for PostgreSQL')
    parser.add_argument('--db', help='Database name for PostgreSQL')
    parser.add_argument('--color', help='Taxi color: green or yellow')
    parser.add_argument('--year', help='Year to ingest data for, e.g., 2021')
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

# How to run
#python ingest_data_automatically.py \
#  --user=root \
#  --password=root \
#  --host=localhost \
#  --port=5433 \
#  --db=ny_taxi \
#  --color=green \
#  --year=2021


