# Use an Ubuntu base image or Debian-based Python image
FROM ubuntu:latest

# Install Python and terminal utilities
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get install -y ncurses-bin && \
    rm -rf /var/lib/apt/lists/*

# Set Python 3 as default
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Create a virtual environment and install dependencies
RUN python -m venv /app/venv
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Set the virtual environment as the default Python environment
ENV PATH="/app/venv/bin:$PATH"

# Run the application
CMD ["python", "your_script.py"]
