# ml-microservices

## Steps to replicate

### docker image build
    $ docker build -t flask:0.0.1 .
    
###  run the container locally:
    $ docker run -p 30002:5000 -it flask:0.0.1

### go to [this page](localhost:30002/)