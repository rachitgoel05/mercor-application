# backend/Dockerfile
# Use the official Python image as a base image
FROM python:3.9-slim
# Copy the requirements file into the container
COPY requirements.txt requirements.txt
# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code into the container
COPY . .
# Specify the command to run the application
CMD ["python", "app.py"]
