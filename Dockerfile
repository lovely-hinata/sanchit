# Use the official Python image as the base image.
# You can specify the Python version as required. Here, we use Python 3.8.
FROM python:3.8-slim

# Set the working directory within the container to /app.
# This is where your application code will reside.
WORKDIR /app

# Copy the requirements.txt file into our working directory /app.
# We do this separately from the rest of the code to leverage Docker caching,
# as dependencies are less likely to change between builds than code.
COPY requirements.txt ./

# Install the Python dependencies specified in requirements.txt.
# Use --no-cache-dir to avoid saving the cache, reducing image size.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container's working directory.
COPY . .

# Specify the command to run on container startup.
# Here, we specify the Python interpreter and the script filename.
CMD ["python", "./Ns_Followers.py"]
