# FastAPI Kafka Microservice

A microservice built with FastAPI that produces/consumes Kafka messages using Confluent kafka and interacts with MySQL + external APIs.

## Run locally

```bash
uvicorn app.main:app --reload