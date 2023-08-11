import os

def check_directory(path):
  files = os.listdir('./')
  
  if files.index(path) == ValueError:
    os.mkdir(path)
  
  
if __name__ == '__main__':
  check_directory('videos')