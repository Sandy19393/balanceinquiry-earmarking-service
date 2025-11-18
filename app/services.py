import requests
from sqlalchemy.orm import Session

from app.config import settings
from app.models import EarmarkTransaction

# Mock balance store
USER_BALANCES = {
    "acc-1001": 500.0,
    "acc-1002": 150.0,
    "acc-1003": 50.0,

}

def check_balance(account_id: str, earmark_amount: float) -> bool:
    balance = USER_BALANCES.get(account_id, 0)
    print(f"Balance check for {account_id}: {balance} >= {earmark_amount}?")
    return balance >= earmark_amount

def save_transaction(db: Session, data: dict, status: str):
    accountId = data.get("debitAccount")
    earmarkAmount = float(data.get("earmarkAmount", 0))
    requestId = data.get("requestId")
    earmarkCurrency = data.get("earmarkCurrency")
    accountBranch = data.get("accountBranch")
    earmarkReference = data.get("earmarkReference")
    businessDate = data.get("businessDate")
    txn = EarmarkTransaction(requestId=requestId, accountId=accountId, earmarkAmount=earmarkAmount, earmarkCurrency=earmarkCurrency, accountBranch=accountBranch, earmarkReference=earmarkReference, businessDate=businessDate, status=status)
    db.add(txn)
    db.commit()
    db.refresh(txn)
    return txn

def call_external_api(data: dict):
    print(f"Calling external API: {settings.EXTERNAL_API_URL}")
    response = requests.post(settings.EXTERNAL_API_URL, json=data, timeout=5)
    print(f"External API Response: {response.status_code}")
    return response.json()