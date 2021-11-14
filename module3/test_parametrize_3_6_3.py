import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestPage:
    links = [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1',
    ]

    def answer(self):
        return math.log(int(time.time()))

    @pytest.mark.parametrize('link', links)
    def test_page(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector('textarea').send_keys(str(self.answer()))
        browser.find_element_by_css_selector('.submit-submission').click()
        result = browser.find_element_by_css_selector('.smart-hints__hint').text
        assert 'Correct!' == result, f'Need "Correct!", got "{result}"'