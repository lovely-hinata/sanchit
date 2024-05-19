# Dockerfile
# Use the official Python image as the base image.
FROM python:3.8-slim

# Set the working directory within the container to /app.
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker cache
# Back4app does not require this step unless your script depends on external libraries.
# If so, ensure you have a requirements.txt file and uncomment the next two lines.
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container's working directory.
COPY . .

# Run the Python script.
CMD ["python", "./Ns_Followers.py"]
