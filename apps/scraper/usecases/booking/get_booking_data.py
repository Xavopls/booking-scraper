from apps.core.services.utils import UtilsService
from apps.scraper.service.booking_scraper_service import BookingScraperService
from apps.scraper.service.selenium_service import SeleniumService


class GetBookingData:

    def __init__(self):
        self.selenium_service = SeleniumService()
        self.scraper_service = BookingScraperService(self.selenium_service)
        self.BASE_URL_NO_DATES = "https://www.booking.com/searchresults.es.html?ss="

    def invoke(self, name: str):
        try:
            # Set up URL
            url = self.BASE_URL_NO_DATES + UtilsService.format_url(name)

            # Scrape and return the booking object
            booking = self.scraper_service.start_scraping(url)

            return booking

        except:
            return False
