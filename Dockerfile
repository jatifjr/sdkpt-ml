# Use the official Python image as the base image
FROM python:3.11.0a1-alpine3.14

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory within the container
WORKDIR /app

# Copy the Poetry dependencies file and install the application dependencies
COPY pyproject.toml poetry.lock /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

# Copy the FastAPI application code into the container
COPY . /app/

# Expose the port your FastAPI app will run on
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
