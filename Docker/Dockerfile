# Base image with Python and essential dependencies
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    cmake \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install \
    torch==2.0.1 \
    torchvision==0.15.2 \
    tensorflow==2.12.0 \
    gym==0.26.2 \
    pettingzoo==1.22.0 \
    ray[rllib]==2.7.1 \
    stable-baselines3==2.0.0 \
    numpy \
    pandas==2.0.3 \
    matplotlib==3.7.1 \
    jupyterlab==4.0.4

# Clone your kindness meta-model repository (replace with your repo)
RUN git clone https://github.com/aamirakbar/SSD_MARL_Kindness.git

# Set environment variables
#ENV PYTHONPATH "${PYTHONPATH}:/app/SSD_MARL_Kindness"
ENV PYTHONPATH=/app/SSD_MARL_Kindness

# Expose Jupyter Lab port
EXPOSE 8888

# Default command to start Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
