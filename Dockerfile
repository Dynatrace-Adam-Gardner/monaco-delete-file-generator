FROM python:slim

WORKDIR /app
COPY generate-delete-file.py .

RUN pip install pyyaml

CMD ["python", "generate-delete-file.py"]
