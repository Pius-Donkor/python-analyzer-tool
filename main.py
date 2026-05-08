from fastapi import FastAPI
from file_analyzer.api.routes import router

app = FastAPI()
app.include_router(router)
