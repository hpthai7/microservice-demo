FROM python:3.7

# Create work directory
RUN mkdir -p /opt/talk-service
WORKDIR /opt/talk-service

# Copy source
COPY ./talk-service/* ./
COPY ./requirements.txt .

# Install python additional packages 
RUN pip3 install -r src/requirements.txt

EXPOSE 5000
CMD gunicorn -b :5000 main:talk_service

