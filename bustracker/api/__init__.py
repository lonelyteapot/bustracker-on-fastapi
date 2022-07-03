from bustracker.api.graphql.context import get_context
from bustracker.api.graphql.schema import schema
from bustracker.api.rest import nodes, routes, stops, types
from bustracker.services.exceptions import ResourceException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from strawberry.fastapi import GraphQLRouter
from uuid_extensions import uuid7

graphql_app = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

app.include_router(types.router)
app.include_router(routes.router)
app.include_router(nodes.router)
app.include_router(stops.router)


@app.get("/uuid")
def get_random_uuid():
    return uuid7()


@app.exception_handler(ResourceException)
async def resource_exception_handler(request: Request, exc: ResourceException):
    return JSONResponse(status_code=exc.status_code, content=exc.asdict())
