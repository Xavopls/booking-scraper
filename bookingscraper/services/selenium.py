from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from django.conf import settings


def init_selenium(url):

    # Selenium WebDriver setup for remote server
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    selenium_url = "http://"+settings.SELENIUM_HOST+":"+settings.SELENIUM_PORT+"/wd/hub"

    # Connect to the remote Selenium server
    driver = WebDriver(
        command_executor=selenium_url,
        options=chrome_options
    )

    # Navigate to the search URL
    driver.get(url)

    # Wait until the page gets fully loaded. OW we get StaleElementException
    sleep(5)

    return driver


def stop_selenium(driver):
    driver.quit()
