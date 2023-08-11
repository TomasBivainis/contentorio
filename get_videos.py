from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 

def get_videos(url):
  options = webdriver.ChromeOptions()
  options.headless = True
  
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
  driver.set_window_size(600, 700)
  
  videos = []
  
  driver.get(url)
  
  button = driver.find_element(By.CSS_SELECTOR, "button.VfPpkd-LgbsSe")
  button.click();

  title = driver.title
  
  #assert title == "Fireship - YouTube"
  
  driver.implicitly_wait(1)
  
  content = driver.find_element(By.ID, 'content').find_elements(By.CSS_SELECTOR, 'ytd-rich-grid-row')
  
  for video in content:
    data = video.find_element(By.ID, 'content').find_element(By.CSS_SELECTOR, "*").find_element(By.ID, "dismissible").find_element(By.ID, 'details').find_element(By.ID, 'meta').find_element(By.CSS_SELECTOR, 'h3').find_element(By.CSS_SELECTOR, 'a')
    
    title = data.get_attribute('title')
    link = data.get_attribute('href')
    
    videos.append([title, link])
      
  driver.quit()
  
  return videos
  
if __name__ == '__main__':
  get_videos("https://www.youtube.com/@Fireship/videos")