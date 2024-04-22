# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install Poetry via pip
RUN pip install poetry

# Copy and install project dependencies using Poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry install

# Copy the project source code into the container
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--log-level", "debug"]
