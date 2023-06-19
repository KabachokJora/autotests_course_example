from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

link = 'https://sbis.ru'
try:
    browser.get(link)
    sleep(1)

    contact_button = browser.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    contact_button.click()
    sleep(1)

    logo_tensor = browser.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    logo_tensor.click()
    sleep(1)

    tabs = browser.window_handles
    browser.switch_to.window(tabs[1])

    block = browser.find_elements(By.CSS_SELECTOR, '.tensor_ru-Index__card')[1]
    assert block.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-title').text == 'Сила в людях'
    block.location_once_scrolled_into_view

    assert block.is_displayed()
    sleep(1)

    more = block.find_element(By.CSS_SELECTOR, '.tensor_ru-link')
    more.click()

    sleep(1)
    assert browser.current_url == 'https://tensor.ru/about'

finally:
    browser.quit()
