# app/main.py

from fastapi import FastAPI

from app.api.v1.router import router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Camufla API",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.include_router(
        router,
        prefix="/api/v1",
    )

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="app.main:app", host="0.0.0.0", port=8080, reload=True)
