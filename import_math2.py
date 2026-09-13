import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Находим сундук и берём valuex
    chest = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    x = chest.get_attribute("valuex")
    y = calc(x)

    # 2. Вводим ответ
    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)

    # 3. Checkbox "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    # 4. Radiobutton "Robots rule!"
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    # 5. Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()