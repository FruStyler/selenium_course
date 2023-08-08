from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    time.sleep(1)
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
