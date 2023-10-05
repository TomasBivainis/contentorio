import os

def check_directory(path):
  files = os.listdir('./')
  path = path.strip('./')
  
  for file in files:
    if file == path:
      return
  
  os.mkdir(path)  
  
if __name__ == '__main__':
  check_directory('videos')