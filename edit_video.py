from moviepy.editor import *
from librosa import load
import os
import soundfile
from pedalboard import Pedalboard, Chorus, Reverb, Distortion, Phaser, Bitcrush, Compressor, Gain
from pedalboard.io import AudioFile
#scipy for painting vfx

os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
VIDEO_PATH = "./videos/"
OUTPUT_PATH = "./output/"
TEMP_PATH = './temp/'


# TODO - finish

def edit_video(title):
  video = VideoFileClip(VIDEO_PATH + title)
  
  #* video editing
  #? maybe tweak some settings or experiment
  
  video = video.fx(vfx.colorx, 100)
  video = video.fx(vfx.gamma_corr, -10)
  video = video.fx(vfx.invert_colors)
  video = video.fx(vfx.lum_contrast, lum=5, contrast=8, contrast_thr=100)
  video = video.fx(vfx.painting, saturation=1.4, black=0.006)
  
  #* audio editing
  
  audio = AudioFileClip(VIDEO_PATH + title)
  audio.write_audiofile(TEMP_PATH + 'temp.mp3')

  #TODO - figure out what effects to use
  
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
  edit_video('Very funny prank-Pilot pretends to falls asleep in airplane.mp4')
  

