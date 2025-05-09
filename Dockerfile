# FROM nginx
# RUN mkdir /etc/nginx
# COPY nginx.conf /etc/nginx

# Python 3.13 slim version for a minimal footprint
FROM python:3.13-slim

# Create the app directory
RUN mkdir /app

# Set working directory for all subsequent commands
WORKDIR /app

# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Ensures Python output is sent straight to terminal without buffering
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

# Install system dependencies:
# libpq-dev: Required for psycopg2 (PostgreSQL adapter)
# gcc: Required for compiling some Python packages
RUN apt-get update \
  && apt-get -y install libpq-dev gcc curl

# Install Node.js using NVM
SHELL ["/bin/bash", "--login", "-c"]
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
RUN nvm install --lts
RUN nvm use --lts

# Install pnpm
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable
RUN wget -qO- https://get.pnpm.io/install.sh | ENV="$HOME/.bashrc" SHELL="$(which bash)" bash -


# Copy requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project to container
COPY . .

# Install Node.js dependencies
RUN pnpm install

# Compile CSS
RUN pnpm tailwind:build

# Expose the Django port
EXPOSE 8004

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.prod.sh

# Set the entrypoint script as the default command
# This will run migrations, collect static files, and start Gunicorn
CMD ["/app/entrypoint.prod.sh"]
