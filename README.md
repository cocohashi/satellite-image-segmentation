# Satelite image segmentation

This repository holds a concept prove of a Satelite image segmentation model development.

### Setup

Docker and docker-compose must be installed

#### Method 1

Run container using docker:
```bash
docker run \
 -p 8888:8888 \
 --name satelite-image-notebook \
 -v [wokdir-path]/notebooks:/home/jovyan/notebooks \
 -e JUPYTER_ENABLE_LAB=yes \
 -it jupyter/minimal-notebook:latest
```
If the container was already created, start it:
```bash
docker start satelite-image-notebook
```
TIP: You can check if you successfully created the container:
```bash
docker ps -a
```
Access to container bash:
```bash
docker exec -it satelite-image-notebook /bin/bash
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

#### Method 2 (recommended)

Create default network (first time only):
```bash
docker network create satelite_image_segmentation_default
```
Navigate to the current project directory path.
Build and up container:
```bash
docker-compose up
```
TIP: If a new package is required:
 - Add it to "requirements.txt" specifying the version 
 - Build new container with "--no-cache" flag active and start container:
```bash
docker-compose build --no-cache
docker-compose up
```
TIP: You can access to console trough given token session in the logs:
```txt
http://127.0.0.1:8888/lab?token=[your-token]
```
