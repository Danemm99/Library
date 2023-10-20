from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_authentication():git
    driver = webdriver.Edge()

    try:
        # Крок 1: Відкриття домашньої сторінки
        driver.get("http://127.0.0.1:8000/")

        time.sleep(3)

        # Крок 2: Клік на кнопці "Увійти"
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Увійти')]")
        login_button.click()

        # Крок 3: Введення вірних облікових даних
        time.sleep(3)

        username_input = driver.find_element(By.ID, "id_email")
        password_input = driver.find_element(By.ID, "id_password")

        username_input.send_keys("danemm99@gmail.com")
        password_input.send_keys("1234")

        time.sleep(2)

        password_input.send_keys(Keys.RETURN)

        time.sleep(3)

        # Крок 4: Перевірка успішного входу
        inf_button = driver.find_element(By.XPATH, "//h2[contains(text(), 'Вітаємо у бібліотеці!')]")
        assert inf_button.is_displayed()

        # Крок 5: Клік на кнопці "Вийти"
        logout_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Вийти')]")
        logout_button.click()

        time.sleep(3)

        # Крок 6: Перевірка успішного виходу
        login_button_again = driver.find_element(By.XPATH, "//button[contains(text(), 'Увійти')]")
        assert login_button_again.is_displayed()

        # Крок 7: Введення невірних облікових даних і перевірка відповідного повідомлення про помилку
        login_button_again.click()

        time.sleep(3)

        username_input = driver.find_element(By.ID, "id_email")
        password_input = driver.find_element(By.ID, "id_password")

        username_input.send_keys("hhh@gmail.com")
        password_input.send_keys("5678")

        time.sleep(3)

        password_input.send_keys(Keys.RETURN)

        time.sleep(3)

        # Крок 8: Перевірка повідомлення про помилку
        error_message = driver.find_element(By.XPATH, "//p[contains(text(), 'Невірна пошта або пароль.')]")
        assert "Невірна пошта або пароль." in error_message.text

        time.sleep(3)

    finally:
        # Закриваємо вікно браузера після виконання тесту
        driver.quit()

# Викликаємо функцію для тестування аутентифікації
test_authentication()



