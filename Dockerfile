FROM python:3.10.4-slim-bullseye

# Install system dependencies
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y git curl wget bash neofetch ffmpeg software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --upgrade pip wheel \
    && pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run the main script as a module
CMD ["python3", "-m", "Banword.banword"]
