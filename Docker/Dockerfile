# Base image with Python and essential dependencies
FROM python:3.9-slim

# Install system dependencies for PyTorch, TensorFlow, and RL libraries
RUN apt-get update && apt-get install -y \
    git \
    cmake \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    patchelf \
    ffmpeg \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Upgrade pip separately to avoid caching issues
RUN pip install --upgrade pip

# Install deep learning frameworks (PyTorch & TensorFlow)
RUN pip install \
    torch==2.0.1 \
    torchvision==0.15.2 \
    tensorflow==2.12.0 

# Install reinforcement learning and multi-agent libraries
RUN pip install \
    gym==0.26.2 \
    pettingzoo==1.22.0 \
    ray[rllib]==2.7.1 \
    stable-baselines3[extra]==2.0.0 \
    sb3-contrib==2.0.0 \
    supersuit

# Install other dependencies for data processing and visualization
RUN pip install \
    numpy \
    pandas==2.0.3 \
    matplotlib==3.7.1 \
    jupyterlab==4.0.4 \
    mujoco-py
    
# Clone your kindness meta-model repository (replace with your repo)
RUN git clone https://github.com/aamirakbar/SSD_MARL_Kindness.git

# Set environment variables
#ENV PYTHONPATH "${PYTHONPATH}:/app/SSD_MARL_Kindness"
ENV PYTHONPATH=/app/

# Expose Jupyter Lab port
#EXPOSE 8888

# Default command to start Jupyter Lab
#CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
CMD ["/bin/bash"]
