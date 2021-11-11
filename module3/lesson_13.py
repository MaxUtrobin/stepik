from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestSunInJuly(unittest.TestCase):

    def test_first(self):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        first_name.send_keys(By.CSS_SELECTOR, "Franco")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        last_name.send_keys("Begbie")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        email.send_keys("begbie@mail.com")
        phone = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
        phone.send_keys("12345678")
        address = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second")
        address.send_keys("Baker str. 13")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_second(self):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        first_name.send_keys(By.CSS_SELECTOR, "Franco")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        last_name.send_keys("Begbie")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        email.send_keys("begbie@mail.com")
        phone = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
        phone.send_keys("12345678")
        address = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second")
        address.send_keys("Baker str. 13")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()