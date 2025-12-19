FROM python:3.12-slim

WORKDIR /app

COPY *.py /app/

RUN pip install --no-cache-dir fastapi uvicorn httpx better-profanity "llm-guard[all]"

EXPOSE 8000

CMD ["uvicorn", "fastAPI:app", "--host", "0.0.0.0", "--port", "8000"]
