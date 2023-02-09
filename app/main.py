from fastapi import FastAPI
from app.api.v1.routes import routes
from dataclasses import dataclass
from typing import List

# https://www.python-httpx.org/advanced/
# https://stackoverflow.com/questions/71031816/how-do-you-properly-reuse-an-httpx-asyncclient-wihtin-a-fastapi-application
# https://www.scrapingbee.com/blog/best-python-http-clients/
# https://curlconverter.com/
# https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/
# https://find-and-update.company-information.service.gov.uk/company/14143549


# Cohesion - the degree to which functions or classes belong together


"""Application entry point."""
app = FastAPI(title="Emilio FastAPI Demo")
app.include_router(router=routes, prefix="/api/v1")


# @dataclass
# class Company:
#     name: str
#     crn: str
#     address: str
#     status: str
#     type: str
#     inc_date: str
#     sic_list: List[str]


# Company(
#     name="ANALYSTS JOURNAL LTD",
#     crn="14143549",
#     address="8 Crown Apartments, 45 Westholme Gardens, Ruislip, England, HA4 8QH",
#     status="Active",
#     type="Private limited Company",
#     inc_date="31 May 2022",
#     sic_list=[
#         "62012 - Business and domestic software development",
#         "62020 - Information technology consultancy activities",
#     ],
# )


# {
#     "name": "ANALYSTS JOURNAL LTD",
#     "crn": "14143549",
#     "address": "8 Crown Apartments, 45 Westholme Gardens, Ruislip, England, HA4 8QH",
#     "status": "Active",
#     "type": "Private limited Company",
#     "inc_date": "31 May 2022",
#     "sic_list": [
#         "62012 - Business and domestic software development",
#         "62020 - Information technology consultancy activities",
#     ],
# }


@app.get("/")
async def root():
    return {"message": "working"}


# @dataclass
# class Account:
#     id: int
#     name: str
#     email: str


# @app.get("/company/{company_id}")
# def find_company(company_id):
#     html = get_company_info(company_id)
#     # name = parse_html_company_house(html)
#     return {"company_id": company_id, "name": html}
