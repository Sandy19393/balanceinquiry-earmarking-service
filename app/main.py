from fastapi import FastAPI, Depends

from app.database import SessionLocal, Base, engine
# from database import Base, engine, SessionLocal
from app.kafka_consumer import start_consumer_thread
from app.kafka_producer import send_message
# from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Balance Inquiry and Earmark Microservice")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    start_consumer_thread()
    return {"status": "Kafka consumer started manually"}

@app.get("/")
def root():
    return {"message": "Kafka + FastAPI + MySQL microservice running"}

@app.post("/produce")
def produce_test_message(data: dict):
    send_message("transactions", data)
    return {"status": "sent", "message": data}
