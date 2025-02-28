from fastapi import FastAPI
import asyncio
import hypercorn.asyncio
from hypercorn.config import Config

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello FastAPI without uvicorn"}

def run():
    config = Config()
    config.bind = ["0.0.0.0:8000"]  # 포트 설정
    asyncio.run(hypercorn.asyncio.serve(app, config))  # 기본 asyncio 사용

if __name__ == "__main__":
    run()
