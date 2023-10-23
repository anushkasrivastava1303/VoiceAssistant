from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class music():
    def __init__(self):
        service = Service(executable_path="C:\\Users\\LENOVO\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe") 
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service , options=options)
    
    def play(self,query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element("xpath", '//*[@id="video-title"]/yt-formatted-string')
        video.click()
        


