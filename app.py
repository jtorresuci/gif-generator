import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

from resize import resize_video
from gifsmall import create_gif

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if not stream:
            raise Exception("No suitable stream found")
        stream.download(output_path)
        return stream.default_filename
    except Exception as e:
        print(f"Failed to download video: {e}")
        return None

def calculate_height(width, original_width, original_height):
    return int((width / original_width) * original_height)

def convert_to_gif(video_path, gif_path, target_width=480):
    try:
        gif_path = resize_video(video_path)
        create_gif(gif_path)

    except Exception as e:
        print(f"Failed to convert video to GIF: {e}")

def main():
    # YouTube URL
    youtube_url = input("Enter youtube url: ")
    
    # Directory to save files
    output_directory = "output"
    os.makedirs(output_directory, exist_ok=True)
    
    # Download the video
    video_filename = download_youtube_video(youtube_url, output_directory)
    if video_filename:
        video_path = os.path.join(output_directory, video_filename)
        
        # Convert to GIF
        gif_filename = os.path.splitext(video_filename)[0] + ".gif"
        gif_path = os.path.join(output_directory, gif_filename)
        print(video_path, gif_path)
        convert_to_gif(video_path, gif_path)
        
        print(f"Video downloaded and converted to GIF: {gif_path}")

if __name__ == "__main__":
    main()
