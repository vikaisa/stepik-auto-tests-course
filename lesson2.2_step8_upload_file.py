import os
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("ivan@example.com")
    
    # получаем путь к директории текущего исполняемого скрипта 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    
    # имя файла, который будем загружать на сайт
    file_name = "example.txt"

    # получаем путь к загружаемому файлу
    file_path = os.path.join(current_dir, file_name)

    element = browser.find_element_by_id("file")
    
    # отправляем файл
    element.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
