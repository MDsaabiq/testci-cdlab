# AI CI/CD Failure Investigator Lab

A very small FastAPI application for practicing CI/CD failure investigation. It exposes `/` and `/health` and includes local tests, a Docker image, an Nginx reverse proxy, and a GitHub Actions workflow.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/health`.

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Run tests locally with:

```bash
pytest app/tests
```

## Run with Docker

```bash
docker compose up --build
```

The API is available at `http://127.0.0.1:8000/health`.

## Test Nginx

With Compose running, Nginx proxies requests to the API at:

```text
http://127.0.0.1:8080/health
```

Stop the containers with `docker compose down`.

## Run GitHub Actions

Push a commit, open a pull request, or select **Run workflow** from the repository's **Actions** tab.

## Create an intentional failure

Change one isolated component at a time, then run the relevant check:

- Break Python: change a return value in `app/main.py`, then run `pytest app/tests`.
- Break dependencies: change a version in `app/requirements.txt`, then run `pip install -r app/requirements.txt`.
- Break Docker: change the base image or `COPY` instruction in `app/Dockerfile`, then run `docker compose build`.
- Break Nginx: change `server app:8000` in `app/nginx/nginx.conf`, then run `docker compose up --build`.
- Break configuration: require an unset environment variable in `app/main.py`, then restart the app.
- Break CI: change a workflow action version or command in `.github/workflows/ci.yml`, then push the change.
