# SmartKMS Queue Test

A lightweight message ingestion pipeline using Redis queues, MongoDB storage, and Python workers to process jobs.

## 1. Prerequisites

- Docker & Docker Compose
- Python 3.10+ (for local development)
- [uv CLI](https://github.com/astral-sh/uv) for environment management

## 2. Local Setup & Run

1. **Clone the repository**:
   ```bash
   git clone git@github.com:lukabele/queue-test.git
   cd queue-test
   ```
2. **Install dependencies** (uses `uv.lock`):
   ```bash
   uv sync
   ```
3. **Run the scripts**:
   ```bash
   uv run python main.py
   uv run python job_handler.py
   uv run python worker.py
   ```

## 3. Docker Compose

Bring up the full stack (Redis, MongoDB, worker):
```bash
docker compose up --build
```

Tear down (remove images, volumes, orphans):
```bash
docker compose down --rmi all --volumes --remove-orphans
```

## 4. Environment Variables

| Variable  | Default                                                    | Purpose                  |
|-----------|------------------------------------------------------------|--------------------------|
| REDIS_URL | `redis://redis:6379`                                       | Redis connection URI     |
| MONGO_URL | `mongodb://root:example@mongo:27017/?authSource=admin`     | MongoDB connection URI   |

## 5. Project Structure

| File                     | Description                             |
|--------------------------|-----------------------------------------|
| `main.py`                | Orchestrates data ingestion flow        |
| `job_handler.py`         | Enqueues jobs into Redis                |
| `worker.py`              | Processes jobs from the queue           |
| `parser.py`              | Normalizes incoming data                |
| `access_drive.py`        | Interfaces with OneDrive API            |
| `test_graph_endpoint.py` | Tests for the Microsoft Graph endpoint  |
| `Dockerfile`             | Builds the application image            |
| `docker-compose.yml`     | Defines Redis, Mongo, and worker services |
| `pyproject.toml`         | Project metadata                        |
| `uv.lock`                | Locked dependencies                     |

## 6. Testing

Run the test suite:
```bash
uv run pytest
```

## 7. Cleanup

Remove Docker artifacts and volumes:
```bash
docker compose down --rmi all --volumes --remove-orphans
```
