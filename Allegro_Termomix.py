# Import of necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager #pip install webdriver_manager

# Test data
product_name = "Termomix"


class WeresaLogin(unittest.TestCase):

    def setUp(self):

        # Test preconditions:

        # Opening the browser:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        # Opening the page:
        self.driver.get("https://allegro.pl/")

        # Maximize the window:
        self.driver.maximize_window()

        # Set to unconditionally wait for an item when searching for a maximum of 10 seconds:
        self.driver.implicitly_wait(10)

    def test_Successful_SignIn(self):
        driver = self.driver

        # STEPS:

        # 1. Click Ok, I agree
        consent = driver.find_element(By.XPATH, "//button[@data-role='accept-consent']")
        consent.click()

        # 2. Enter something
        looking = driver.find_element(By.XPATH, "//input[@data-role='search-input']")
        looking.send_keys(product_name)
        looking = driver.find_element(By.XPATH, "//button[@data-role='search-button']")
        looking.click()

        # 3. Search for items on 1 page with the word "Termomix"
        termomix = driver.find_elements(By.XPATH, "//article[@data-role='offer']")
        self.assertEqual(len(termomix), 73, "There should be 73 items in the list")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)