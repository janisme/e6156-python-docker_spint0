# python-docker

A simple Python app for [Docker's Python Language Guide](https://docs.docker.com/language/python).

# Source

- Based on Donald Ferguson's github :https://github.com/donald-f-ferguson/python-docker

## Run a simple test. without decker

```
# This is not necessary becaise I am in the directory
# cd /path/to/python-docker

# Create a virtual environment. https://docs.python.org/3/library/venv.html
python3 -m venv .venv

# Activate the virtual environment.
source .venv/bin/activate

# Install dependencies. This is an example of one of the 12 Factor Rules --> Declare dependencies.
(.venv) $ python3 -m pip install -r requirements.txt

# Run the application and access from a browser, run the flask development server.
(.venv) $ python3 -m flask run #run a flask module
or
(.venv) $  python3 app.py

# CNTL-C to end application

# Exit virtual environment.
deactivate
```

## Docker

- Using command to build Docker.
  - docker init
    ```? What application platform does your project use? Python
    ? What version of Python do you want to use? 3.11
    ? What port do you want your app to listen on? 5000
    ? What is the command to run your app? flask run --host 0.0.0.0 ```
    
    - create:
      - Dockerfile : a text document that contains all the commands a user could call on the command line to assemble an image.
      - .dockerignore: to exclude files and directories from the build context.
      - compose.yaml: used to configure your Docker application’s services, networks, volumes, and more.w
  - Commands:
    - ```docker compose up --build  ``` run the app
    - ```docker compose up --build -d```, ```docker compose down``` run in background



- Wrote the docker files following a old school example.  https://medium.com/geekculture/how-to-dockerize-your-flask-application-2d0487ecefb8
  - dockerfile:
    - first import python from dockerhub.
    - create working dir
    - copy the requirement
    - run requirement to install all the dependencies
    - copy the entire project
    - expose port 5000 as the app will run on port 5000.
    - Define the FLASK_APP environment variable. Else the interpreter may complain it’s unable to find the variable
    - Type in the run command which is flask run --host 0.0.0.0. This is to ensure the server accepts requests from all hosts.
  
  - Commands:
    - ```docker build -t janisme/e6156-flask .``` #build a docker image from current dirc(.) and tag it with name.
    - ```docker images``` 
    - ```docker run -p 5001:5001 janisme/e6156-flask```
    - ```docker push janisme/e6156-flask``` (This step pushed an image for your architecture)

## EC2

- There are several services like EC2, ECS, Fargate, and EKS to run Docker containers on AWS.
- I used an Amazon Linux instance.


- I followed this example: https://medium.com/appgambit/part-1-running-docker-on-aws-ec2-cbcf0ec7c3f8
  - ```sudo yum update -y```
  - ```sudo yum install docker```
- Activate docker
  - ```sudo service docker start```
  - ```sudo usermod -a -G docker ec2-user```
  - make sure you installed Git.

- Pull docker and run a docker container
  - ```docker pull janisme/e6156-flask```
  - ```sudo docker run -p (-d) 5001:5001 janisme/e6156-flask ``` #-d use as background, port 5001 on the host machine to port 5001 in the container, janisme/e6156-flask: a docker image to use to create a container

- Used ```curl localhost:5001``` #remember to set the network security group, 'curl':making HTTP requests
- Go into the console and get the EC2 instances public IP address. You can now access the app on 5001.


## Some Helpful Commands

- Kill a process on a port (MacOS): ```lsof -i tcp:3000```
- see which caontainer is in use ```docker ps```
- kill container ```docker stop container_id ```
