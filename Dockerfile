# Use the official Python base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Install necessary dependencies
RUN apk add --no-cache bash

# Copy the alertsClient script into the container
COPY alertsClient.py /app/alertsClient.py

# Install required Python packages
RUN pip install --no-cache-dir paho-mqtt

# Set the default entrypoint to the Python script and allow passing arguments
ENTRYPOINT ["python", "/app/alertsClient.py"]
