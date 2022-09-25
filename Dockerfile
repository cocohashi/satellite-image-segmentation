# base ===========================================================================

FROM jupyter/minimal-notebook:latest AS satelite-image-segmentation-base

WORKDIR notebooks

# Install Pip packages
COPY notebooks/requirements.txt notebooks/requirements.txt
RUN pip install --no-cache-dir -r notebooks/requirements.txt