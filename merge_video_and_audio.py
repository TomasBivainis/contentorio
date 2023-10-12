import ffmpeg
from moviepy.editor import *
import os

os.environ["IMAGEIO_FFMPEG_EXE"] = "./ffmpeg"

def merge_video_and_audio(title):
  
  video = VideoFileClip('./temp/video.mp4')
  audio = AudioFileClip('./temp/audio.mp4')
  
  video.set_audio(audio)
  
  video.write_videofile('./videos/' + title + '.mp4')
  
  # os.remove('./temp/video.webm')
  # os.remove('./temp/audio.webm')

if __name__ == '__main__':
  merge_video_and_audio('test')