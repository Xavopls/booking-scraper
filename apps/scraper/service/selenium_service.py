from time import sleep
from typing import Optional
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.conf import settings


class SeleniumService:

    def __init__(self):
        # Initialize any instance variables if needed
        self.driver: Optional[WebDriver] = None

    def init_selenium(self, url: str) -> WebDriver:
        """
        Initializes the Selenium WebDriver and navigates to the provided URL.
        """
        try:
            # Setup Chrome options
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")

            selenium_url = f"http://{settings.SELENIUM_HOST}:{settings.SELENIUM_PORT}/wd/hub"

            # Connect to the remote Selenium server
            self.driver = WebDriver(
                command_executor=selenium_url,
                options=chrome_options
            )

            # Navigate to the search URL
            self.driver.get(url)

            # Wait until the page gets fully loaded
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))  # Wait for the body tag to load
            )

            return self.driver

        except Exception as e:
            print(f"Error initializing Selenium: {e}")
            raise

    def stop_selenium(self) -> None:
        """
        Stops the Selenium WebDriver.
        """
        if self.driver:
            try:
                self.driver.quit()
            except Exception as e:
                print(f"Error stopping Selenium: {e}")
                raise
