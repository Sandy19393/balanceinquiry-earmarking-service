from confluent_kafka import Producer
import json
from app.config import settings

producer = Producer({"bootstrap.servers": settings.KAFKA_BOOTSTRAP_SERVERS})

def send_message(topic: str, message: dict):
    json_message = json.dumps(message).encode('utf-8')
    producer.produce(topic, value=json_message)
    producer.flush()
    print(f"Produced message to {topic}: {json_message}")
