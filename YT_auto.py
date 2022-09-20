from selenium import webdriver
from selenium.webdriver.common.by import By

class music():
    def __init__(self):
        self.driver=webdriver.Chrome()
    def play(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        vedio= self.driver.find_element(By.XPATH,value='//*[@id="video-title"]')
        vedio.click()

