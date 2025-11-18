from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class EarmarkTransaction(Base):
    __allow_unmapped__ = True
    __tablename__ = "earmark_transactions"


    id= Column(Integer, primary_key=True, index=True)
    requestId : Mapped[str] = mapped_column(String(30), nullable=False)
    accountId : Mapped[str] = mapped_column(String(50), nullable=False)
    earmarkAmount : Mapped[float] = mapped_column(Float, nullable=False)
    earmarkCurrency : Mapped[str] = mapped_column(String(3), nullable=False)
    accountBranch : Mapped[str] = mapped_column(String(3), nullable=False)
    earmarkReference : Mapped[str] = mapped_column(String(30))
    businessDate : Mapped[str] = mapped_column(String(20))
    status = Column(String(20), default="pending")
    created_at = Column(DateTime, server_default=func.now())
