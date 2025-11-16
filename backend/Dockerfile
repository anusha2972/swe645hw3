# Team members:
# 1. Anusha Gurram – G01514835
# 2. Bala Naga Tirumala Kiran Annadata – G01508483
# 3. Yashwanth Karthikeya Settem– G01512992

# Creates the Docker image for the FastAPI app and runs it with Gunicorn and Uvicorn.



FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app


RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY app ./app


RUN useradd -u 10001 -m appuser

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000


HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -fsS http://127.0.0.1:8000/healthz || exit 1


CMD ["gunicorn", "app.main:app", \
     "-k", "uvicorn.workers.UvicornWorker", \
     "-w", "2", "-b", "0.0.0.0:8000", \
     "--access-logfile=-", "--error-logfile=-"]
