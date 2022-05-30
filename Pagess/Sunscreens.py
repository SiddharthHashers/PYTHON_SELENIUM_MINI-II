from selenium.webdriver.common.by import By


class Sunscreenspage:
    Sunscreens_product1 = "/html[1]/body[1]/div[1]/div[2]/div[1]/p[1]"
    Sunscreens_add = "//body/div[1]/div[2]/div[1]/button[1]"
    Addcart = "//button[@onclick='goToCart()']"
    Product_cart="//table[@class='table table-striped']/tbody/tr/td[1]"
    price_cart="//table[@class='table table-striped']/tbody/tr/td[2]"
    paywithcard = "//span[contains(text(),'Pay with Card')]"
    def __init__(self,driver):
        self.driver=driver

    def gettextsunscreensproduct1(self):

        self.sunscreensproduct1 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/p[1]")
        self.gettextsunscreensproduct2 = self.sunscreensproduct1.text

        self.sunscreensprice1 = self.driver.find_element(By.XPATH, "//div[@class='container']/div[2]/div[1]/p[2]")
        self.gettextsunscreensprice1 = self.sunscreensprice1.text
        return self.gettextsunscreensproduct2,self.gettextsunscreensprice1

    def Addproduct1(self):
        self.Addproduct1 = self.driver.find_element(By.XPATH,"//body/div[1]/div[2]/div[1]/button[1]")
        self.Addproduct1.click()

    def Addcart1(self):
        self.Addcart = self.driver.find_element(By.XPATH,"//button[@onclick='goToCart()']")
        self.Addcart.click()
        lst = self.driver.window_handles
        for i in lst:
            self.driver.switch_to.window(i)
        self.price_cart = self.driver.find_element(By.XPATH,"//table[@class='table table-striped']/tbody/tr/td[2]")
        #self.paywithcard = "//span[contains(text(),'Pay with Card')]"
        self.Product_cart=self.driver.find_element(By.XPATH,"//table[@class='table table-striped']/tbody/tr/td[1]")

        self.pricecarttext=self.price_cart.text
        self.productcarttext = self.Product_cart.text
        return self.pricecarttext,self.productcarttext

    def paywithcard(self):
        self.pay=self.driver.find_element(By.XPATH,"//span[contains(text(),'Pay with Card')]")
        self.pay.click()