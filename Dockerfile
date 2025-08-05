# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy everything into container
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies by scanning all Python files in /app/src
RUN python config/deps.py

# Set src as the working code directory
WORKDIR /app/src

# Run the main script
CMD ["python", "main.py"]
