#!/bin/bash

sh -c './wait-for db:5432 -- npm start'  # doesnt work nc command is missing!

sleep 30  # wait for bd

celery -A app.worker.celery_app worker -l INFO --concurrency=2 -B