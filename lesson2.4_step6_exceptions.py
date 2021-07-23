from selenium import webdriver
import time

browser = webdriver.Chrome()

try: 
    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element_by_id("button")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

