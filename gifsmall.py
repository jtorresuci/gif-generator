from moviepy.editor import VideoFileClip, vfx

def create_gif(video_path):
    # Load the video file
    video = VideoFileClip(video_path)

    # Specify the duration of the GIF: start at 0 seconds and end at 60 seconds
    # If the video is shorter than 60 seconds, it will end at the video's end
    clip_duration = min(int(input("Enter clip duration: ")), video.duration)  # Ensure we do not exceed the video length
    video_clip = video.subclip(int(input("Enter clip start: ")), clip_duration)
    video_clip = video_clip.fx(vfx.speedx, 20)  # Increase speed by a factor of 2

    # Set the fps (frames per second) for the GIF
    fps = 200

    # Path to save the GIF
    gif_path = video_path.replace('.mp4', '.gif')  # Adjust the path accordingly

    # Write the GIF file from the 60-second clip
    video_clip.write_gif(gif_path, fps=fps)

    print(f"GIF saved successfully at {gif_path}")
