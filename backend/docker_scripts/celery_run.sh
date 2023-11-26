#!/bin/bash
sleep 15
cd /code
celery -A app.worker.celery_app worker -l info -B