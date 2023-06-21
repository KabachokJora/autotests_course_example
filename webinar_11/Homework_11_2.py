from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep
import datetime

browser = webdriver.Chrome()
action = ActionChains(browser)

link = 'https://fix-online.sbis.ru/'

user_login = 'ivanovma'
user_password = 'ivanov123'
try:
    browser.get(link)
    browser.maximize_window()
    sleep(1)

    login_field = browser.find_element(By.CSS_SELECTOR, "[name='Login']")
    login_field.send_keys(user_login, Keys.ENTER)

    password_field = browser.find_element(By.CSS_SELECTOR, "[name='Password']")
    password_field.send_keys(user_password, Keys.ENTER)
    sleep(1)

    browser.get('https://fix-online.sbis.ru/page/dialogs/')
    sleep(1)

    me = browser.find_element(By.CSS_SELECTOR, '[name="item-myProfile"]').text

    add_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    add_button.click()
    sleep(2)

    search_field = browser.find_element(By.CSS_SELECTOR, '.addressee-selector-popup__browser-search input')
    search_field.send_keys(me)
    sleep(1)

    users = browser.find_elements(By.CSS_SELECTOR, '.msg-addressee-selector__addressee')
    sleep(1)

    action.move_to_element(users[0])
    action.click(users[0])
    action.perform()

    sleep(1)

    message_field = browser.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    message_text = f'Привет! Это тестовое сообщение {datetime.datetime.now()}'
    message_field.send_keys(message_text)
    sleep(1)

    send_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    assert send_button.is_displayed(), 'Отсутствует кнопка отправки сообщения'
    send_button.click()
    sleep(2)

    messages_list = browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert messages_list[0].text == message_text, 'Палундра! Текст не совпадает'

    action.move_to_element(messages_list[0]).perform()
    browser.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]').click()
    sleep(1)

    messages_list = browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert messages_list[0].text != message_text, 'Палундра! Сообщение не удалили!'


finally:
    browser.quit()
