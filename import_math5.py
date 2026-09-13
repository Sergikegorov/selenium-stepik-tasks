import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Заполняем текстовые поля
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@example.com")

    # 2. Загружаем файл
    # Путь к папке, где лежит текущий скрипт
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "example.txt")

    # Создаём пустой файл, если его нет
    with open(file_path, "w") as f:
        pass

    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(file_path)

    # 3. Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()