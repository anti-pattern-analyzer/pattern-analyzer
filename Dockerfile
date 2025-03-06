# Use a minimal Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full application
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app (adjust import path)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
