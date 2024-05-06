FROM python:3.11

# Install htop
RUN apt-get update && apt-get install -y htop

# Create workapp directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Bundle app source
COPY . /app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
