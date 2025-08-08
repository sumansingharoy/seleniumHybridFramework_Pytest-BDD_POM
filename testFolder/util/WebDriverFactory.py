from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver


class WebDriverFactory:
    def get_driver(self, config):
        browser_name = config['browser'].lower()
        headless = config.get('headless', False)

        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--window-size=1920,1080')
            if headless:
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument('--no-sandbox')

            driver = webdriver.Chrome(options=options)

        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--width=1920')
            options.add_argument('--height=1080')
            if headless:
                options.add_argument('--headless')

            driver = webdriver.Firefox(options=options)

        else:
            raise Exception(f"Browser '{browser_name}' is not supported. Use 'chrome' or 'firefox'.")

        return driver
