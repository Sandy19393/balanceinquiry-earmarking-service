import json
import threading
from confluent_kafka import Consumer, KafkaError

from app.config import settings
from app.database import SessionLocal
from app.services import check_balance, save_transaction, call_external_api


def process_message(data: dict):
    accountId = data.get("debitAccount")
    earmarkAmount = float(data.get("earmarkAmount", 0))

    db = SessionLocal()
    try:
        if check_balance(accountId, earmarkAmount):
            txn = save_transaction(db, data, "approved")
            call_external_api(data)
        else:
            save_transaction(db, data, "rejected")
            print(f"Transaction rejected for {accountId}")
    finally:
        db.close()

def consume_messages():
    consumer_conf = {
        "bootstrap.servers": settings.KAFKA_BOOTSTRAP_SERVERS,
        "group.id": "balance-consumer-group",
        "auto.offset.reset": "earliest",
    }

    consumer = Consumer(consumer_conf)
    consumer.subscribe([settings.KAFKA_TOPIC])

    print("Kafka consumer started...")

    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() != KafkaError._PARTITION_EOF:
                print(f"Kafka error: {msg.error()}")
            continue

        try:
            data = json.loads(msg.value().decode("utf-8"))
            print(f"Consumed message: {data}")
            process_message(data)
        except Exception as e:
            print(f"Error processing message: {e}")

def start_consumer_thread():
    thread = threading.Thread(target=consume_messages, daemon=True)
    thread.start()
