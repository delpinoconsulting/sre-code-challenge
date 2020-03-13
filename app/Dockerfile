# Get official Python Docker image
FROM python:3.6

# Default Flask port
EXPOSE 5000

WORKDIR /app

# Install any required dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Run app.py when the container launches
COPY main.py /app
CMD python main.py