# Use a lightweight Python image
FROM python:3.9-slim-buster

# Install FFmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Install pip, setuptools, and wheel
RUN python3 -m pip install -U pip setuptools wheel

# Install yt-dlp
RUN python3 -m pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the yewtube package
RUN pip install yewtube

# Run the command to start the terminal in interactive mode
CMD ["bash"]
