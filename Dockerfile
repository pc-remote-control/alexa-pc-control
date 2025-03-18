# Use Python 3.9
FROM python:3.9  

# Set working directory inside the container
WORKDIR /app  

# Copy all files from your repo to the container
COPY . /app  

# Install dependencies (from requirements.txt)
RUN pip install -r requirements.txt  

# Run the Flask app
CMD ["python", "app.py"]
