# Use the official Python image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . /app

# Install required packages
RUN pip install -r requirements.txt

# Expose the port that your FastAPI app will run on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
