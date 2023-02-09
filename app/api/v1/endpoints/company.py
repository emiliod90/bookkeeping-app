from fastapi import APIRouter, HTTPException, Path
from app.services.v1.company_info import scrape_company_info_service
from app.api.v1.schemas.company_schema import LtdCompany, LtdCompanyBase

route = APIRouter(
    prefix="/company",
    tags=["company"],
    responses={404: {"description": "Not found"}},
)


@route.get("/{company}", response_model=LtdCompanyBase)
def find_company(company: str = Path(title="The 8 Character Company Number to search")):
    company_info = scrape_company_info_service(company_number=company)
    return company_info


@route.post("/")
def check_company(company: LtdCompany):
    return {"message": "Company is valid", "company": company}
