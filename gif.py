from moviepy.editor import VideoFileClip

# Path to the source video
video_path = 'output/resized_video.mp4'  # Adjust the path accordingly

# Load the video file
video = VideoFileClip(video_path)

# Set the fps (frames per second) for the GIF
fps = 30

# Path to save the GIF
gif_path = video_path.replace('.mp4', '.gif')  # Adjust the path accordingly

# Write the GIF file
video.write_gif(gif_path, fps=fps)

print(f"GIF saved successfully at {gif_path}")
