# Satelite image segmentation

This repository holds a concept prove of a Satelital image segmentation model development.

### Setup

#### Method 1:

Run container using docker:
```bash
docker run \
 -p 8888:8888 \
 --name satellite-image-notebook \
 -v [wokdir-path]/notebooks:/home/jovyan/notebooks \
 -e JUPYTER_ENABLE_LAB=yes \
 -it jupyter/minimal-notebook:latest
```
If the container was already created, start it:
```bash
docker start satellite-image-notebook
```
TIP: You can check if you successfully created the container:
```bash
docker ps -a
```
Access to container bash:
```bash
docker exec -it satellite-image-notebook /bin/bash
```
From container (Ex. jovyan@5fe5aa456726), install required libraries:
```bash
pip install -r notebooks/requirements.txt
```
To start jupyter notebook in your browser, a token session will be needed. Print available jupyter servers:
```bash
jupyter server list
```
This will print accessible servers. Ex:
```txt
Currently running servers:
http://5fe5aa456726:8888/?token=[your-token] :: /home/jovyan
```
Copy this URL an insert into your browser changing current "CONTAINER ID" by "localhost":
```txt
http://localhost:8888/?token=[your-token]
```
NOTE: If this is the first time you have created the container, a new token session will be created,
so you will only need to access to it:\
http://localhost:8888


