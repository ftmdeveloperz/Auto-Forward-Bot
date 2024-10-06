# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the necessary port if your bot listens on one (optional)
# EXPOSE 5000  # For example, if you have a web interface

# Command to run your bot
CMD ["python", "bot.py"]
