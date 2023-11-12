# Use an official Python runtime as the parent image
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Install NLTK and PRAW using pip
RUN pip install nltk praw

# Download NLTK data (you may need to download specific datasets)
RUN python -c "import nltk; nltk.download('punkt')"

# Copy your Python application code into the container (if you have any)
COPY . /app

# Specify the command to run your Python application (replace with your script)
CMD [ "python", "your_script.py" ]
