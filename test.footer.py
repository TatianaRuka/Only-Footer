import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestFooter:

    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://only.digital/")
        yield
        self.driver.quit()

    def test_footer_presence(self, setup):
        # Проверка наличия футера на главной странице
        footer = self.driver.find_element(By.TAG_NAME, "footer")
        assert footer is not None, "Футер не найден на странице"

    def test_footer_elements(self, setup):
        footer = self.driver.find_element(By.TAG_NAME, "footer")

        # Проверяем наличие конкретных элементов
        elements_to_check = [
            "//a[contains(text(), 'Начать проект')]",
            "//a[contains(text(), 'Creative digital production')]",
            "//a[contains(text(), 'Only.digital')]",
            "//a[contains(text(), 'Создаем digital-продукт на базе стратегии, креатива и технологий.')]",
            "//a[contains(text(), '2024')]",
            "//a[contains(text(), '+7 (495) 740 99 79')]"
            "//a[contains(text(), 'hello@only.com.ru')]",
            "//p[contains(text(), '©')]"
        ]

        for xpath in elements_to_check:
            element = footer.find_element(By.XPATH, xpath)
            assert element is not None, f"Элемент по xpath '{xpath}' не найден в футере"

    @pytest.mark.parametrize("url", [
        "https://only.digital/",
        "https://only.digital/company?award=Рейтинг+Рунета",  # проверка чпсти футера на странице наград
    ])
    def test_footer_on_multiple_pages(self, setup, url):
        self.driver.get(url)

        # Проверка наличия футера
        footer = self.driver.find_element(By.TAG_NAME, "footer")
        assert footer is not None, f"Футер не найден на странице {url}"

        # Проверка элементов в футере
        elements_to_check = [
            "//a[contains(text(), 'Начать проект')]",
            "//a[contains(text(), '2024')]"
        ]

        for xpath in elements_to_check:
            element = footer.find_element(By.XPATH, xpath)
            assert element is not None, f"Элемент по xpath '{xpath}' не найден на странице {url}"

# Для запуска тестов используйте команду:
# pytest test_footer.py
