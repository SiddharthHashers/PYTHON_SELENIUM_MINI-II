from selenium.webdriver.common.by import By
#from Pages.Homepage import Homepage
from Pagess.Sunscreens import Sunscreenspage
#from Testcases.TestHomepage import Test_001_homepage

class Test_003_Testsunscreenspage:

    def test_sunscreenspage(self,setup):
        #self.hp = Homepage(self.driver)
        #self.testhp = Test_001_homepage(self.driver)
        self.driver = setup
        self.sp = Sunscreenspage(self.driver)
        self.text1,self.text2=self.sp.gettextsunscreensproduct1()
        #self.text1=self.testhp.a
        print(self.text1)
        print(self.text2)
        self.sp.Addproduct1()
        self.price,self.product=self.sp.Addcart1()
        print("#")
        print(self.product)
        print(self.price)
        if (self.text1 == self.product):
            assert True

            self.sp.paywithcard()


        else:
            assert False
