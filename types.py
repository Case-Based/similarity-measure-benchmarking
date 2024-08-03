from dataclasses import dataclass
from typing import Optional
from enum import Enum


class TransactionType(Enum):
    CASH_IN = 1
    CASH_OUT = 2
    DEBIT = 3
    PAYMENT = 4
    TRANSFER = 5


@dataclass
class DataEntry:
    step: int
    transaction_type: int
    amount: float
    name_origin: str
    old_balance_origin: float
    new_balance_origin: float
    name_destination: str
    old_balance_destination: float
    new_balance_destination: float
    is_fraud: Optional[int]

