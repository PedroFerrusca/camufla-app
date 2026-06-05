# Camufla

## Introduction

Camufla is the backend server for the Camufla game platform.

Use this service together with the mobile application to host and play a family-friendly social deduction game inspired by Chameleon / Impostor-style gameplay.

Supported game sessions:

* 4 to 12 players
* Private game rooms
* Real-time game state synchronization
* Multiplayer session management

---

## Local Development

### Prerequisites

Before starting, make sure you have installed:

1. Python 3.12 or newer
2. `uv`
3. Docker (or any compatible container runtime)

---

### Install Dependencies

After cloning the repository:

```shell
uv venv
source .venv/bin/activate   # Linux / macOS

# Windows
# .venv\Scripts\activate

uv sync
```

---

### Start Local Services

Start PostgreSQL:

```shell
docker compose up --build db
```

The `--build` flag is only required the first time or after container configuration changes.

Run in detached mode:

```shell
docker compose up -d db
```

---

### Run the Application

Start the development server:

```shell
uv run python -m app.main
```

Once running, access:

```text
API:        http://localhost:8000
Swagger UI: http://localhost:8000/docs
OpenAPI:    http://localhost:8000/openapi.json
```

---

## Development Workflow

Install new dependencies:

```shell
uv add <package>
```

Install development dependencies:

```shell
uv add --dev <package>
```

Update dependencies:

```shell
uv sync
```

---

## Project Status

🚧 Early development — APIs and database schema may change frequently.
