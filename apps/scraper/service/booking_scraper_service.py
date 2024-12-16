from selenium.webdriver.common.by import By
from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from apps.core.models.booking import Booking


class BookingScraperService:
    def __init__(self, selenium_service):
        self.selenium_service = selenium_service
        self.driver: Optional[WebDriver] = None

    def start_scraping(self, url: str):
        self.driver = self.selenium_service.init_selenium(url)
        return self._scrape_booking_hotel()

    def _stop(self):
        if self.driver:
            self.selenium_service.stop_selenium(self.driver)

    def _scrape_booking_hotel(self):
        try:
            # Extract hotel data from the page
            hotel_elements = self.driver.find_elements(By.CSS_SELECTOR, "div[data-testid='property-card']")
            if hotel_elements:
                return self._handle_hotel(hotel_elements[0])
            else:
                return False
        except Exception as e:
            print(f"Error scraping hotel data: {e}")

            return False

    def _handle_hotel(self, hotel):
        """Extract and handle specific hotel details."""
        # Scrape the hotel's data
        try:
            name = hotel.find_element(By.CSS_SELECTOR, "div[data-testid='title']").text
        except:
            name = "N/A"

        try:
            location = hotel.find_element(By.CSS_SELECTOR, "span[data-testid='address']").text
        except:
            location = "N/A"

        # Review score (handle case when it's not available)
        try:
            review_score_element = hotel.find_element(By.CSS_SELECTOR, "div[data-testid='review-score'] .ac4a7896c7").text
            review_mark = float(review_score_element.replace("Puntuación: ", "").replace(",", "."))
        except:
            review_mark = 0.0

        # Number of comments (handle case when it's not available)
        try:
            comment_amount_element = hotel.find_element(By.CSS_SELECTOR, "div.abf093bdfe.f45d8e4c32.d935416c47").text.split(" ")[0]
            comment_amount = int(comment_amount_element.replace(".", ""))
        except:
            comment_amount = 0

        # Photo URLs (handle case when they're not available)
        photo_urls = []
        try:
            photo_element = hotel.find_element(By.CSS_SELECTOR, 'img[data-testid="image"]')
            photo_url = photo_element.get_attribute('src')
            photo_urls.append(photo_url)
        except:
            pass

        # Description (handle case when it's not available)
        try:
            description = hotel.find_element(By.CSS_SELECTOR, "div.abf093bdfe:not(.ecc6a9ed89)").text
        except:
            description = ""

        # Average price (if available in the data)
        average_price = 0.0

        # Return the extracted data as a Booking
        return {
            "name": name,
            "location": location,
            "average_price": average_price,
            "description": description,
            "review_mark": review_mark,
            "number_of_comments": comment_amount,
            "photo_urls": photo_urls,
            "amenities": []
        }
