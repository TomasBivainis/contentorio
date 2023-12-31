import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "./ffmpeg"
from moviepy.editor import *
from pedalboard import Pedalboard, Chorus, Reverb, Distortion, Phaser, Bitcrush, Compressor, Gain
from pedalboard.io import AudioFile
from check_directory import check_directory 

os.environ["IMAGEIO_FFMPEG_EXE"] = "./ffmpeg"
VIDEO_PATH = "./videos/"
OUTPUT_PATH = "./output/"
TEMP_PATH = "./temp/"

def merge_video(title):
  video = VideoFileClip('./temp/video.mp4')
  audio = AudioFileClip('./temp/audio.mp4')
  
  video.set_audio(audio)
  
  video.write_videofile('./videos/' + title + '.mp4')

def edit_video(title):
  video = VideoFileClip(VIDEO_PATH + title)
  
  #* video editing
  
  video = video.fx(vfx.colorx, 100)
  video = video.fx(vfx.gamma_corr, -10)
  video = video.fx(vfx.invert_colors)
  video = video.fx(vfx.lum_contrast, lum=5, contrast=8, contrast_thr=100)
  video = video.fx(vfx.painting, saturation=1.4, black=0.006)
  
  #* audio editing
  
  audio = AudioFileClip(VIDEO_PATH + title, buffersize = 9999999999999999) 
  audio.write_audiofile(TEMP_PATH + 'temp.mp3', write_logfile = True)
  
  board = Pedalboard([Distortion(drive_db=25), Gain(gain_db=1), Chorus(rate_hz=1, depth=0.25, centre_delay_ms=7, feedback=0, mix=0.5), Phaser(rate_hz=1, depth=0.5, centre_frequency_hz=1300, feedback=0, mix=0.5)])
  # Distortion()
  # Chorus()
  # Bitcrush()
  # Compressor()
  
  with AudioFile(TEMP_PATH + 'temp.mp3') as f:
    
    with AudioFile(TEMP_PATH + 'output.mp3', 'w', f.samplerate, f.num_channels) as o:
    
      while f.tell() < f.frames:
        chunk = f.read(f.samplerate)
        
        effected = board(chunk, f.samplerate, reset=False)
        
        o.write(effected)
  
  audio = AudioFileClip(TEMP_PATH + 'output.mp3')
  
  audio = audio.fx(afx.volumex, 0.3)
  
  video = video.set_audio(audio)
  
  for file in os.listdir(TEMP_PATH):
    os.remove(TEMP_PATH + file)
  
  video.write_videofile(OUTPUT_PATH + title)

if __name__ == '__main__':
  check_directory(VIDEO_PATH)
  
  unedited_videos = os.listdir(VIDEO_PATH)
  edited_videos = os.listdir(OUTPUT_PATH)
  
  print(unedited_videos)
  print(edited_videos)
  
  for video in unedited_videos:
    if video in edited_videos:
      pass
    else:
      edit_video(video)
  

