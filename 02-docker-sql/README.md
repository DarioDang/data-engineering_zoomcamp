# Introduction 

This folder demonstrates how to extract data from external sources and load it into a PostgreSQL database. It utilizes Docker Compose to containerize two key services: a PostgreSQL database and pgAdmin, a graphical interface for executing SQL queries and managing the database. The project showcases the setup of a data pipeline that includes data ingestion, database initialization, and SQL-based data manipulation using pgAdmin as the primary interface.


# 1. Install Docker & Docker Compose

- Skip if already installed
    - "brew install docker docker-compose"

# 2. Clone the repository

- "git clone https://github.com/your-username/your-repo.git"
- "cd your-repo"

# 3. Create pg-network

- "docker network create pg-network"

# 4. To map the local folder with folder in container in docker (mounting)

docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5433:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13

# 5. To run the docker compose contain 2 containers: pg-database, pgAdmin 

docker-compose up 
