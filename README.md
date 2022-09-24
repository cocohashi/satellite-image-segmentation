# Satelite image segmentation

This repository holds a concept prove of a Satelital image segmentation model development.

### Setup

Run container using docker:
```bash
docker run
 -p 8888:8888
 --name satellite-image-notebook
 -v [wokdir-path]/notebooks:/home/jovyan/notebooks
 -e JUPYTER_ENABLE_LAB=yes
 -it jupyter/minimal-notebook:latest
```

