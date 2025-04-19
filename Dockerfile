# Use official Python image
FROM python:3.10

# Avoid buffer issues and force real-time logs
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


# Set working directory
WORKDIR /portfolio_project

# Install system dependencies required for common Python packages like Pillow
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libfreetype6-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy project files into the container
COPY . .

# Collect static files (if needed)
RUN python manage.py collectstatic --noinput

# Expose the port Django will run on
EXPOSE 80

# Start the Django development server
CMD ["sh", "-c", "python manage.py migrate && gunicorn portfolio_project.wsgi:application --bind 0.0.0.0:80"]
