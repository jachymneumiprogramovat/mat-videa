import os
import subprocess
from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys

qual = str(sys.argv[1])
if qual not in ["l","m","h"]:
    raise ValueError(f"there is no such video quality as {qual}")

cur_dir = os.getcwd()
video = cur_dir.split("/")[len(cur_dir.split("/"))-1]

quality = {"l":"480p15",
           "m":"720p30",
           "h":"1080p60"}

path = f"{cur_dir}/media/videos/{video}/{quality[qual]}/"

try:
    subprocess.run(["ls",f"{path}"],check=True,capture_output=True)
except:
    raise ValueError("There is no generated video with this quality")

try:
    subprocess.run(["rm",f"{path}final.mp4"])
except:  
    print("first final video of its kind")

vid_list = []
for filename in os.listdir(path):
    if filename.endswith('.mp4'):
        file_path = os.path.join(path, filename)
        vid_list.append(file_path)
vid_list.reverse()


clips = [VideoFileClip(video) for video in vid_list]

# Concatenate clips
final_clip = concatenate_videoclips(clips, method="compose")

# Write the result to a file
final_clip.write_videofile(f'{path}{video}.mp4', codec="libx264")
