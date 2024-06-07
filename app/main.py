from fastapi import FastAPI

app = FastAPI()

from app.components.compressor.router import router as compressor
from app.components.redirect.router import router as redirect

app.include_router(compressor)
app.include_router(redirect)

