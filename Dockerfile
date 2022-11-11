# base ===========================================================================

FROM jupyter/minimal-notebook:latest AS satellite-image-segmentation-base

WORKDIR notebooks

USER root
# Install Pip packages
COPY notebooks/requirements.txt notebooks/requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir -r notebooks/requirements.txt