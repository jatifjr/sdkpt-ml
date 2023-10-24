# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN python3 -m venv .venv
RUN source .venv/bin/activate
RUN pip install -r requirements.txt

# Expose port 80 for the API
EXPOSE 80

# Run the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
