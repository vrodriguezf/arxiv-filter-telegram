# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot script and .env file
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Run the bot
CMD ["python", "bot.py"]