import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#from pageobjects.Homepage import Homepage

#from POMAssignment.Pages import Homepage
from Pagess.Homepages import Homepage
from TestPage.Test_Moisturizers  import Test_002_Testmoistuizerspage
from TestPage.Test_Sunscreens import Test_003_Testsunscreenspage
from selenium.webdriver.chrome.options import Options
#from Pages.Homepage import Homepage
from selenium.webdriver.chrome.service import Service
#import Homepage
from Pagess.Logger import LogGen

#hp=POMAssignment.Pages.Homepage.Homepage()
class Test_001_homepage:
    URL="https://weathershopper.pythonanywhere.com/"
    logger = LogGen.loggen()

    def test_homepage(self,setup):
        self.driver=setup
        #self.options = webdriver.ChromeOptions()
        #self.options.add_experimental_option("detach", True)
        #self.driver=webdriver.Chrome(chrome_options=self.options, executable_path=r'/Users/nelangovan/PycharmProjects/PomAssignment/Driver/chromedriver')
        self.driver.get(self.URL)
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.logger.info("****Opening URL****")
        self.hp=Homepage(self.driver)
        title = self.driver.title
        print(title)
        if (title == "Current Temperature"):
            assert True
            self.logger.info("****Login test passed ****")

        else:
            assert False
        self.text=self.hp.gettemperature()
        print(self.text)
        if(int(self.text)>25):
            self.hp.buysunscreeens()
            print("sunscreen")
            lst = []
            lst = self.driver.window_handles
            for i in lst:
                self.driver.switch_to.window(i)
            self.a=self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/p[1]")
            print(self.a.text)
            title=self.driver.title
            if(title=="The Best Sunscreens in the World!"):
                assert True
                self.logger.info("****Login test passed ****")

                time.sleep(5)
                self.tsp = Test_003_Testsunscreenspage()
                self.tsp.test_sunscreenspage(setup)
            else:
                assert False
        else:
            self.hp.buymosturizers()
            print("mosturizers")
            lst = []
            lst = self.driver.window_handles
            for i in lst:
                self.driver.switch_to.window(i)
            self.a = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/p[1]")
            print(self.a.text)
            title = self.driver.title
            if (title == "The Best Moisturizers in the World!"):
                assert True
                time.sleep(5)
                self.thp = Test_002_Testmoistuizerspage()
                self.thp.test_moistuizerspage(setup)
            else:
                assert False



