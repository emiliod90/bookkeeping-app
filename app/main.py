from fastapi import FastAPI
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup

app = FastAPI(title="Emilio FastAPI Demo")

@app.get("/")
async def root():
    return {"message": "working"}

@dataclass
class Account:
    id: int
    name: str
    email: str

@dataclass
class Company:
    id: str
    name: str
    address: str
    status: str
    type: str
    date: str





@app.get("/company/{company_id}")
async def find_company(company_id):
    return {"company_id": company_id}
