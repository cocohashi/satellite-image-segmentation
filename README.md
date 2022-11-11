# Satellite image segmentation

This repository holds a customized implementation of a U-Net model in Pytorch for Kaggle's 
[Aerial Semantic Segmentation Drone Dataset](https://www.kaggle.com/datasets/bulentsiyah/semantic-drone-dataset).

The projects aim to establish a common ground tool for any satellite image segmentation task.

### Setup

For methods 1 and 2 Docker and docker-compose must be installed

#### Method 1

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
docker start satelite-image-notebook
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

#### Method 2 (recommended)

Create default network (first time only):
```bash
docker network create satellite_image_segmentation_default
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

#### Method 3 (Using Anaconda Distribution)

The methods above, do not provide CUDA environment to train models using GPU.
This methods instead, provides a solution to can train models enabling GPU.

You need to:
 - [Install 'nvidia-cuda-tookit'](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
 - Test installation:
```bash
nvidia-smi 
 ```
 - [Install Anaconda Distribution](https://docs.anaconda.com/anaconda/install/linux/)
 - Create a new environment:\
TIP [Conda Cheat-Sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

```bash
 conda create --name img-seg python=3.8
 ```
 - Start environment and install Jupyter-lab:
```bash
conda activate img-seg
conda install -c anaconda jupyter
 ```
 - Install all requirements from root project path:
```bash
 pip install -r notebooks/requirements.txt
 ```

#### Resources

Interesting resources to set 'nvidia-container-runtime' on Docker container:
 - [Install nvidia-container-runtime](https://docs.docker.com/config/containers/resource_constraints/#gpu)
 - [Setup GPU within a Docker Container](https://towardsdatascience.com/how-to-properly-use-the-gpu-within-a-docker-container-4c699c78c6d1)
 - [How to Use an NVIDIA GPU with Docker Containers](https://www.howtogeek.com/devops/how-to-use-an-nvidia-gpu-with-docker-containers/)
 - [gpu-jupyter image](https://hub.docker.com/r/cschranz/gpu-jupyter)

[A collection of Satellite image datasets](https://github.com/chrieke/awesome-satellite-imagery-datasets)
