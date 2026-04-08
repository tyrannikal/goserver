FROM python:3.12-slim
COPY main.py main.py
COPY books/ books/
CMD ["python", "main.py"]
