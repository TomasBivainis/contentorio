import argparse
from check_directory import check_directory
from pytube import YouTube
from edit_video import merge_video
import os

HIGHEST_QUALITY = '1080p'
VIDEO_SAVE_PATH = "./videos"
TEMP_PATH = './temp'

def download(video_url):
  yt = YouTube(video_url)

  #print(yt.streams.filter(progressive=True, mime_type="video/mp4"))
  
  video = yt.streams.filter(mime_type="video/mp4")[0]
  
  if len(yt.streams.filter(res = HIGHEST_QUALITY, file_extension = 'mp4')) > 0:
    video = yt.streams.filter(res = HIGHEST_QUALITY, file_extension = 'mp4')[0]
  else:
    video = yt.streams.filter(file_extension = 'mp4')[0]
  
  #print(yt.streams.filter(only_audio=True, file_extension='mp4'))
  
  audio = yt.streams.filter(only_audio=True, file_extension='mp4')[len(yt.streams.filter(only_audio=True, file_extension='mp4'))-1]
  
  
  #print(video)
  #print(audio)
  
  try:
      video.download(output_path=TEMP_PATH, filename='video.mp4')
      audio.download(output_path=TEMP_PATH, filename='audio.mp4')
      merge_video(yt.title)
      os.remove('./temp/video.mp4')
      os.remove('./temp/audio.mp4')
  except:
      print('Died')
      return False
    
if __name__ == '__main__':
  list = ['https://www.youtube.com/watch?v=1s8Kdc6AGT8', 'https://www.youtube.com/watch?v=zcVwkQ_ZjJw', 'https://www.youtube.com/watch?v=lSTgA8pEc8w']
  
  download('https://www.youtube.com/watch?v=KwC16WlpYWQ')