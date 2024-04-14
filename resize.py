import os
import moviepy.editor as mp


def resize_video(video_path):
    # Check if the file exists
    if not os.path.exists(video_path):
        print(f"File not found: {video_path}")
    else:
        print(f"File exists: {video_path}")
        # Load the video file
        video = mp.VideoFileClip(video_path)

        # Resize the video
        # The height is set to None to maintain aspect ratio automatically
        resized_video = video.resize(width=900)

        resized_video_str = video_path.replace('.mp4', ' - resized video.mp4')
        # Write the resized video to a new file
        resized_video.write_videofile(resized_video_str, codec='libx264')

        return resized_video_str