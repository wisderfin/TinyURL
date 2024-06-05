from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def main():
    return RedirectResponse(url="https://google.com"), {"hello": "world"}

