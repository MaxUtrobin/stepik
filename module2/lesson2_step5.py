from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)
field = browser.find_element(By.CSS_SELECTOR, '#answer')
field.send_keys(y)
checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
checkbox.click()
radio_button = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
radio_button.click()
button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
button.click()
time.sleep(30)
browser.quit()

