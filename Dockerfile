FROM python:3.12-slim
WORKDIR /lab
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY app /lab/app
CMD ["python", "/lab/app/service.py", "delivery"]
