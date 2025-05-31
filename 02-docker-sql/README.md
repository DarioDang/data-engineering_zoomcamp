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
