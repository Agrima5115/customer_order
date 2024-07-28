# Use a Python base image
FROM python:3.11.9

# Set the working directory
WORKDIR /app

# Copy the application code
COPY app/app.py .
COPY app/test_app.py .
COPY app/orders.csv .

# Install any required packages
RUN pip install pandas psycopg2-binary redis

# Set a default command
CMD ["python", "app.py"]
