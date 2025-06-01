import pandas as pd
import os
from sqlalchemy import create_engine
import argparse 
import pyarrow

# Write a script to ingest data into PostgreSQL
def main(params):
    "Write a script to ingest data into PostgreSQL"
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    parquet_name = 'output.parquet'
    os.system(f"wget {url} -O {parquet_name}")
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    df = pd.read_parquet(parquet_name)
    df.head(n=0).to_sql(name= table_name, con = engine, if_exists = 'replace')
    df.to_sql(name=table_name, con = engine, if_exists = 'append')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest data into PostgreSQL')
    parser.add_argument('--user', help = 'User name for PostgreSQL')
    parser.add_argument('--password', help = 'Password for PostgreSQL')
    parser.add_argument('--host', help = 'Host for PostgreSQL')
    parser.add_argument('--port', help = 'Port for PostgreSQL')
    parser.add_argument('--db', help = 'Database name for PostgreSQL')
    parser.add_argument('--table_name', help = 'Table name for PostgreSQL')
    parser.add_argument('--url', help = 'URL of the parquet file to ingest')
    args = parser.parse_args()
    main(args)

# Example usage:
# URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"
#python ingest_data.py \
#  --user=root \
#  --password=root \
#  --host=localhost \
#  --port=5433 \
#  --db=ny_taxi \
#  --table_name=yellow_taxi_data \
#  --url=${URL}



