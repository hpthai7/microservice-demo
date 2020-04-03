FROM python:3.7

# Create app directory
RUN mkdir -p /opt/user-service
WORKDIR /opt/user-service

# Bundle app source
COPY ./src ./src
COPY ./main.py .

#Install python additional packages 
RUN pip3 install -r src/requirements.txt

EXPOSE 5000
CMD gunicorn -b :5000 main:user_service

