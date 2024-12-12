
from bookingscraper.services.scraper import scrape_booking_hotel
from bookingscraper.services.selenium import init_selenium, stop_selenium

BASE_URL_NO_DATES = "https://www.booking.com/searchresults.es.html?ss="


def invoke(name):
    try:
        # Set up URL
        url = get_url(name)

        # Init selenium driver
        driver = init_selenium(url)

        # Scrape and return
        hotel = scrape_booking_hotel(driver)
        # End selenium session
        stop_selenium(driver)

        return hotel

    except:
        return False


def get_url(name: str):
    if not name:
        raise ValueError("Name cannot be None or empty.")
    # Check if RFC 1738 encoded
    formatted_name = name.replace("%20", "+").lower()
    return BASE_URL_NO_DATES + formatted_name