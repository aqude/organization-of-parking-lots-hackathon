#!/bin/bash
sleep 15
celery -A app.celery worker --loglevel=info