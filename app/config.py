import os

class Settings:
    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "transactions")

    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "MySql@12345")
    MYSQL_DB = os.getenv("MYSQL_DB", "transaction")

    EXTERNAL_API_URL = os.getenv("EXTERNAL_API_URL", "http://localhost:8001/earmark")

settings = Settings()