# FastAPI Kafka Microservice

A microservice built with FastAPI, that consumes earmarking requests from payment processors, performs balance inquiry and earmarking by connecting to downstream APIs.
This is integrated with Confluent Kafka, MySQL and external service API 

## Run locally

```bash
uvicorn app.main:app --reload