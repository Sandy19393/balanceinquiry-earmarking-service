from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

encodedPassword = quote_plus(settings.MYSQL_PASSWORD)
print(f"Encoded password {encodedPassword}")
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{settings.MYSQL_USER}:{encodedPassword}"
    f"@{settings.MYSQL_HOST}/{settings.MYSQL_DB}"
)
print(f"DAtabase url formed {SQLALCHEMY_DATABASE_URL}")
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
