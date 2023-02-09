from typing import List
from pydantic import BaseModel, validator
from datetime import datetime


class ClientBase(BaseModel):
    name: str
    country: str
    postcode: str


class Client(ClientBase):
    vat: str

    class Config:
        schema_extra = {
            "example": {
                "name": "AMAZON EU SARL, UK BRANCH",
                "address": "38 Avenue John F. Kennedy, Luxembourg 1855, Luxembourg",
                "iso_country": "LU",
                "status": "Active",
                "type": "Private limited Company",
                "crn": "14143549",
                "inc_date": "31/05/2022",
                "accounts_date": "31/05/2023",
                "sic_list": [
                    "62012 - Business and domestic software development",
                    "62020 - Information technology consultancy activities",
                ],
            }
        }
