# Routes - URI path used to access the available endpoints
from fastapi import APIRouter

from app.api.v1.endpoints import company

routes = APIRouter()

routes.include_router(company.route)
