FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create templates directory and add HTML file
RUN mkdir -p templates

# Create simple HTML template
RUN echo '<!DOCTYPE html><html><head><title>Weather App</title></head><body><h1>Weather App</h1><form action="/weather" method="POST"><input type="text" name="city" placeholder="Enter city name" required><button type="submit">Get Weather</button></form></body></html>' > templates/index.html

EXPOSE 5000

CMD ["python", "app.py"]
