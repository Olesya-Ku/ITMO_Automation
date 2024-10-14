from selenium import webdriver
from selenium.webdriver.common.by import By


def check_elements():

    driver = webdriver.Chrome()

    try:
        # Переход на страницу
        driver.get("https://www.saucedemo.com/")

        # Поиск элементов
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.CSS_SELECTOR, ".btn_action")

        # Условие для проверки найденных элементов
        if username_field and password_field and submit_button:
            print("Элементы найдены")

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        # Закрываем драйвер
        driver.quit()


# Вызов функции
check_elements()