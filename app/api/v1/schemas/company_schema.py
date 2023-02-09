from typing import List
from pydantic import BaseModel, validator
from datetime import datetime


class CompanyBase(BaseModel):
    name: str
    address: str
    status: str
    type: str


class LtdCompanyBase(CompanyBase):
    crn: str
    inc_date: str
    accounts_date: str
    sic_list: List[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "ANALYSTS JOURNAL LTD",
                "address": "8 Crown Apartments, 45 Westholme Gardens, Ruislip, England, HA4 8QH",
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


# external_date = {'name': 'ANALYSTS JOURNAL LTD', 'crn': '14143549', 'address': '8 Crown Apartments, 45 Westholme Gardens, Ruislip, England, HA4 8QH', 'status': 'Active', 'type': 'Private limited Company', 'inc_date': '31 May 2022', 'sic_list': ['62012 - Business and domestic software development', '62020 - Information technology consultancy activities']}


# LtdCompanyBase(name='ANALYSTS JOURNAL LTD',crn='14143549',address='8 Crown Apartments, 45 Westholme Gardens, Ruislip, England, HA4 8QH',status='Active',type='Private limited Company',inc_date='31 May 2022',sic_list=['62012 - Business and domestic software development', '62020 - Information technology consultancy activities'])


class LtdCompany(LtdCompanyBase):
    """
    LtdCompany Schema
    ----------
    A pydantic schema to enforce validation on Post requests using the LtdCompany Entity.
    The validator is a class method (cls) which refers to the class, not the object
    """

    @validator("type")
    def validate_type(cls, value):
        if value != "Private limited Company":
            raise ValueError("Private limited Company type only accepted")
        return value

    @validator("inc_date", "accounts_date")
    def validate_date(cls, value):
        if datetime.strptime(value, "%d/%m/%Y"):
            return value
        else:
            raise ValueError("Date not valid")

    @validator("crn")
    def validate_crn(cls, value):
        if len(value) != 8:
            raise ValueError("Company Number (CRN) should be 8 characters in length")
        return value


# CRN Length
# ----------
# The CRN is made up of up to eight numerals or normally two alphabetical characters referred to as the prefix followed by up to six alphanumeric characters, the suffix.
# https://www.gov.uk/hmrc-internal-manuals/cotax-manual/com40011


# LtdCompany(**request)

# https://www.cheapaccounting.co.uk/blog/index.php/what-is-a-year-end-or-accounting-reference-period/#:~:text=The%20year%20end%20for%20your,31st%20December%20or%2031st%20March.
