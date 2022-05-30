from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Homepage:
    #Current_temperature="//span[@id='temperature']"
    Buy_moisturizers="//button[contains(text(),'Buy moisturizers')]"
    Buy_sunscreens="//button[contains(text(),'Buy sunscreens')]"

    def __init__(self,driver):
        self.driver=driver
        self.Buy_sunscreens=""
        self.Buy_moisturizers=""
        self.Current_temperature=""
    def gettemperature(self):
        self.currenttemperature=self.driver.find_element(By.XPATH,"//span[@id='temperature']")
        self.current=self.currenttemperature.text
        self.lst=self.current.split()
        print(self.lst)
        print(self.lst[0]+"new")
        return self.lst[0]

    def buymosturizers(self):
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Buy moisturizers')]").click()

    def buysunscreeens(self):
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Buy sunscreens')]").click()