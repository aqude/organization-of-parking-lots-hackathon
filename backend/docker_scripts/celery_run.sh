#!/bin/bash
sleep 30
celery -A app.celery worker --loglevel=info