from fastapi import FastAPI
from mangum import Mangum

from apps.backend import clusters
from apps.backend.containers import Container

container = Container()
container.wire(modules=[clusters])

app = FastAPI()
app.container = container
app.include_router(clusters.router, prefix="/clusters")

lambda_handler = Mangum(app, api_gateway_base_path="api", lifespan="off")
