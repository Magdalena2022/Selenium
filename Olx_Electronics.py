# Import of necessary libraries
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class OLXElectronics(unittest.TestCase):

    def setUp(self):

        # Test preconditions:

        # Opening the browser:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        # Opening the page:
        self.driver.get("https://www.olx.pl/")

        # Maximize the window:
        self.driver.maximize_window()

        # Set to unconditionally wait for an item when searching for a maximum of 10 seconds:
        self.driver.implicitly_wait(10)

    def test_Successful_Search_For_Multiple_Elements(self):
        driver = self.driver

        # STEPS:

        # 1. Click Accept next to the message
        accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept.click()
        sleep(3)

        # 2. Click "Electronics"
        electronics = driver.find_element(By.PARTIAL_LINK_TEXT, "Elektronika")
        electronics.click()

        # 3. Click "Photo"
        photo = driver.find_element(By.PARTIAL_LINK_TEXT, "Fotografia")
        photo.click()

        elements = driver.find_elements(By.XPATH, "//div[@class='css-1sw7q4x']")
        self.assertEqual(len(elements), 53, "There should be 53 items in the list")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)