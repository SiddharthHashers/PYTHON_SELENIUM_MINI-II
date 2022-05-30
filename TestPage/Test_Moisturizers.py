from selenium.webdriver.common.by import By
#from Pages.Homepage import Homepage
#from Testcases.TestHomepage import Test_001_homepage
from Pagess.Moisturizers import  Moistuizerspage
class Test_002_Testmoistuizerspage:

    def test_moistuizerspage(self,setup):
        #self.hp = Homepage(self.driver)
        #self.testhp = Test_001_homepage(self.driver)
        self.driver=setup
        self.mp = Moistuizerspage(self.driver)
        self.text1,self.text2=self.mp.gettextMoistuizerproduct1()
        #self.text1 = self.testhp.a
        print(self.text1)
        print(self.text2)
        self.mp.Addproduct1()
        self.price,self.product=self.mp.Addcart1()
        print("#")
        print(self.product)
        print(self.price)
        if(self.text1==self.product):
            assert True

            self.mp.paywithcard()

        else:
            assert False
