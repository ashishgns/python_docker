# Use the official Python image.
FROM python:3.11-slim

# Set the working directory.
WORKDIR /usr/src/app

# Copy requirements file and install dependencies.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . .

# Expose the port the app runs on.
EXPOSE 8000

# Define the command to run the app.
CMD ["python", "main.py"]
