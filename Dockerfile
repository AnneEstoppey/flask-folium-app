# this is an official Python runtime, used as the parent image
FROM python:3.7.3-slim

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# copy your app folder into docker image so our app can run within the docker container
COPY . /app

# unblock port 80 for the Flask app to run on
EXPOSE 80

# execute the Flask app
CMD ["python", "app.py"]