# Dockerfile
FROM python:3.12-slim

# Data
LABEL maintainer="siuda.mateo@gmail.com"\
      version="1.0"\
      description="Discord bot"\
      environment="src"

# Define the workdir on the container
WORKDIR /src

# Run user without cache
RUN adduser --disabled-password --gecos "" --uid 1000 appuser

# Copy requirements.txt
COPY requirements.txt .

# Run dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy every files from project
COPY . .

# Install procps for HEALTHCHECK (contains pgrep)
RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

# Change user
RUN chown -R appuser:appuser /src

# Switch to non-root user
USER appuser

# Define envs
ENV PYTHONUNBUFFERED=1\
    PORT=25921

# Expose port
EXPOSE $PORT

# HEALTHCHECK (endpoint src)
HEALTHCHECK --interval=60s \
            --timeout=1s \
            --start-period=60s \
            --retries=3 \
            CMD pgrep -f "main.py" || exit 1

# Run the bot
CMD [ "python", "main.py"]