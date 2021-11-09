from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    first_name = browser.find_element_by_css_selector(".first_block .form-control.first")
    first_name.send_keys("Franco")
    last_name = browser.find_element_by_css_selector(".first_block .form-control.second")
    last_name.send_keys("Begbie")
    email = browser.find_element_by_css_selector(".first_block .form-control.third")
    email.send_keys("begbie@mail.com")
    time.sleep(1)
    phone = browser.find_element_by_css_selector(".second_block .form-control.first")
    phone.send_keys("12345678")
    time.sleep(1)
    address = browser.find_element_by_css_selector(".second_block .form-control.second")
    address.send_keys("Baker str. 13")
    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()