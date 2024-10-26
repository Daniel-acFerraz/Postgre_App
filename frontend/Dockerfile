# Use an official Python runtime as a parent image
FROM python:3.12.2-slim

# Set the working directory in the container to /app
WORKDIR /app

# dont write pyc files
# dont buffer to stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy code from application to container
COPY  ./frontend/requirements.txt /tmp/requirements.txt

# Install pipenv
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8502

# Run main.py when the container launches
ENTRYPOINT ["streamlit", "run", "frontend/app/main.py", "--server.port", "8502", "--server.address", "0.0.0.0"]