# Use a supported Debian version
FROM python:3.10.4-slim-bullseye

# Update and install necessary packages
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y git curl wget bash neofetch ffmpeg software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --upgrade pip wheel \
    && pip3 install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Run the app
CMD ["python3", "-m", "MAFU"]
