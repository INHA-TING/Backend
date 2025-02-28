FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /Backend

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# FastAPI 앱 실행 (uvicorn 없이)
CMD ["python", "main.py"]
