from fastapi import FastAPI
from mangum import Mangum

from apps.backend.routers import router

app = FastAPI()

app.include_router(router, prefix="/clusters")

lambda_handler = Mangum(app, api_gateway_base_path="api", lifespan="off")
