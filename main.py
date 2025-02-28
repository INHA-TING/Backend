#ASGI 서버 실행 스크립트
from fastapi import FastAPI
import asyncio
import hypercorn.asyncio
from hypercorn.config import Config

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "FastAPI without uvicorn"}

def run():
    config = Config()
    config.bind = ["0.0.0.0:8000"]  # 포트 설정
    asyncio.run(hypercorn.asyncio.serve(app, config))

if __name__ == "__main__":
    run()
