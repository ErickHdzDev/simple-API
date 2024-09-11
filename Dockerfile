FROM python:3.10-slim

RUN apt-get update && apt-get install -y git

WORKDIR /app

ARG GIT_TOKEN

RUN git clone https://github.com/ErickHdzDev/simple-API.git

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]