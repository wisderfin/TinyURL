from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешаем доступ со всех источников
origins = ["*"]

# Настраиваем CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

from app.backend.components.compressor.router import router as compressor
from app.backend.components.redirect.router import router as redirect

app.include_router(compressor)
app.include_router(redirect)

