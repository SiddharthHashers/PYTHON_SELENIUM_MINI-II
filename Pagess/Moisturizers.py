
from selenium.webdriver.common.by import By

class Moistuizerspage:
    Moistuizer_product1="/html/body/div[1]/div[2]/div[1]/p[1]"
    Moistuizer_add="/html/body/div[1]/div[2]/div[1]/button"
    Addcart="//button[@onclick='goToCart()']"
    Product_cart = "//table[@class='table table-striped']/tbody/tr/td[1]"
    price_cart="//table[@class='table table-striped']/tbody/tr/td[2]"
    paywithcard="//span[contains(text(),'Pay with Card')]"
    def __init__(self,driver):
        self.driver=driver
    def gettextMoistuizerproduct1(self):

        self.Moistuizerproduct1 = self.driver.find_element(By.XPATH, "//div[@class='container']/div[2]/div[1]/p[1]")
        self.gettextMoistuizerproduct2 = self.Moistuizerproduct1.text
        self.Moistuizerprice1 = self.driver.find_element(By.XPATH, "//div[@class='container']/div[2]/div[1]/p[2]")
        self.gettextMoistuizerprice1 = self.Moistuizerprice1.text
        return self.gettextMoistuizerproduct2,self.gettextMoistuizerprice1

    def Addproduct1(self):
        self.Addproduct1 = self.driver.find_element(By.XPATH,"//body/div[1]/div[2]/div[1]/button")
        self.Addproduct1.click()

    def Addcart1(self):
        self.Addcart = self.driver.find_element(By.XPATH,"//button[@onclick='goToCart()']")
        self.Addcart.click()
        lst = self.driver.window_handles
        for i in lst:
            self.driver.switch_to.window(i)

        self.price_cart = self.driver.find_element(By.XPATH,"//table[@class='table table-striped']/tbody/tr/td[2]")
        self.Product_cart=self.driver.find_element(By.XPATH,"//table[@class='table table-striped']/tbody/tr/td[1]")
        #self.paywithcard = "//span[contains(text(),'Pay with Card')]"
        self.pricecarttext = self.price_cart.text
        self.productcarttext = self.Product_cart.text
        return self.pricecarttext,self.productcarttext

    def paywithcard(self):
        self.pay=self.driver.find_element(By.XPATH,"//span[contains(text(),'Pay with Card')]")
        self.pay.click()