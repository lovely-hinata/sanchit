FROM python:3.9

WORKDIR /usr/src/app

# Install dependencies
RUN pip install -r requirements.txt

# Copy the code
COPY . .

# Run the app
CMD ["python", "Ns_Followers.py"]
