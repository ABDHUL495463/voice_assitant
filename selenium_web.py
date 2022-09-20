from selenium import webdriver
from selenium.webdriver.common.by import By

class infow():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search= self.driver.find_element(By.XPATH,value='//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element(By.XPATH,value='//*[@id="search-form"]/fieldset/button')
        enter.click()



