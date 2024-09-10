# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py main.py

ENV PYTHONUNBUFFERED=1
ENV TOKEN=""
ENV CHAT_ID=""

# Run the Python script when the container launches
CMD ["python", "./main.py"]
