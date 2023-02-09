from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    address: str
    VATREG: str
