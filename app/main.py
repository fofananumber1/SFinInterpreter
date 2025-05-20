from fastapi import FastAPI
from app import routes

app = FastAPI(title="Finance Interpreter")

app.include_router(routes.router)