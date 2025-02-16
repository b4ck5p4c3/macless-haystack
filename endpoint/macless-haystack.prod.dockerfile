FROM python:slim

RUN apt-get update && apt-get install -y curl nano iproute2 cron

COPY . /app/endpoint
WORKDIR /app

# Configure python
RUN pip install --no-cache-dir -r endpoint/requirements.txt
# Update server files on startup
CMD ["sh", "-c", "python3 -u endpoint/mh_endpoint.py"]