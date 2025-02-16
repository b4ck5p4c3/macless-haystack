FROM python:slim

RUN apt-get update && apt-get install -y curl nano iproute2 cron

COPY . /endpoint
WORKDIR /endpoint

# Configure python
RUN pip install --no-cache-dir -r requirements.txt
# Update server files on startup
CMD ["sh", "-c", "python mh_endpoint.py"]