#!/bin/bash
sleep 30  # wait for bd
celery -A app.worker.celery_app worker -l INFO --concurrency=2 -B
