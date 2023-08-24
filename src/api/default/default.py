from fastapi import APIRouter, Response, Request

default_router = APIRouter()


@default_router.get("/health")
async def health() -> Response:
    return Response(status_code=200)


@default_router.get("/")
async def home() -> Response:
    return Response(content='{"message": "Hello World"}', status_code=200)


@default_router.get("/version")
def last_version(request: Request) -> Response:
    return Response(
        content=f'{{"version": "{request.app.state.version}"}}', status_code=200
    )
