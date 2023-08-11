import argparse
from pytube import YouTube

HIGHEST_QUALITY = '1080p'
VIDEO_SAVE_DIRECTORY = "./videos"

def download(video_url):
  video = YouTube(video_url)

  if len(video.streams.filter(res = HIGHEST_QUALITY, file_extension = 'mp4')) > 0:
    video = video.streams.filter(res = HIGHEST_QUALITY, file_extension = 'mp4')[0]
  else:
    video = video.streams.get_highest_resolution()
  
  try:
      video.download(VIDEO_SAVE_DIRECTORY)
      return True
  except:
      return False
    
if __name__ == '__main__':
  download('https://www.youtube.com/watch?v=1s8Kdc6AGT8')