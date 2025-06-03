# 1. Use official Python 3.8 image as base
FROM python:3.9-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy requirements.txt into container
COPY requirements.txt .


# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all app files into container
COPY model.pkl .
COPY species_map.pkl .
COPY . .

# 6. Expose port 5000 for the Flask app
EXPOSE 5000

# 7. Command to run the app
CMD ["python", "run.py"]
