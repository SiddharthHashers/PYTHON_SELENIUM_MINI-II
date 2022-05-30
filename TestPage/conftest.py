import pytest
from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(chrome_options=options, executable_path=r'/Users/sikalidas/PycharmProjects/Mini_Assignment_CheckTemp/Drivers/chromedriver')
    return driver
