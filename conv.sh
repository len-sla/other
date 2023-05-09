#!/bin/bash

# Check if the /root/mps directory exists in the container
if ! docker exec yewtube [ -d /root/mps ]; then
  echo "The /root/mps directory does not exist in the container"
  exit 1
fi

# Loop through all WebM files in the /root/mps directory and convert them to MP4 and MP3
docker exec yewtube find /root/mps -type f -name "*.webm" | while read file; do
  # Get the filename without the extension
  filename=$(basename -- "$file")
  extension="${filename##*.}"
  filename="${filename%.*}"

  # Convert the WebM file to MP4 using ffmpeg
  # docker exec yewtube ffmpeg -i "$file" -c:v libx264 -preset slow -crf 22 -c:a copy "/root/mps/${filename//[^[:alnum:]]/_}.mp4" # first version generating 0 bytes
  docker exec yewtube ffmpeg -i "$file" -c:v libx265 -crf 28 -c:a aac -b:a 128k "/root/mps/${filename//[^[:alnum:]]/_}.mp4"


  # Extract the audio stream as an MP3 file using ffmpeg
  docker exec yewtube ffmpeg -i "$file" -vn -c:a libmp3lame -q:a 2 "/root/mps/${filename//[^[:alnum:]]/_}.mp3"

  # Remove the original WebM file
  docker exec yewtube rm "$file"
done
