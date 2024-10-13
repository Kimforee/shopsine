# Use the official Python image, specify version 3.11
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose port 8000 for Django
EXPOSE 8000

# Run the Django app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "shopsine.wsgi:application"]