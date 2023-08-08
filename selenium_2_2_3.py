from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num_1 = int(num1.text)
    num2 = browser.find_element(By.ID, "num2")
    num_2 = int(num2.text)
    y = str(num_1 + num_2)
    print(num_1, num_2, y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
