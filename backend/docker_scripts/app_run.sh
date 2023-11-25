#!/bin/bash 
sleep 30 # wait for bd
cd /code/app/db 
alembic upgrade head
cd ../../
gunicorn app.__main__:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 