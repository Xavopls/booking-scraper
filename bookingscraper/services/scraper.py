
from selenium.webdriver.common.by import By

from bookingscraper.dtos.bookingdto import BookingDto

BASE_URL_NO_DATES = "https://www.booking.com/searchresults.es.html?ss="


def scrape_booking_hotel(driver):
    try:
        # Extract hotel data
        hotel_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='property-card']")
        if hotel_elements:
            return handle_hotel(hotel_elements[0])
        else:
            return False
    except Exception as e:
        print(e)
        return False


def handle_hotel(hotel):
    # Scrape the hotel's data
    name = hotel.find_element(By.CSS_SELECTOR, "div[data-testid='title']").text

    location = hotel.find_element(By.CSS_SELECTOR, "span[data-testid='address']").text

    try:
        review_score_element = hotel.find_element(By.CSS_SELECTOR, "div[data-testid='review-score'] .ac4a7896c7").text
        review_mark = float(review_score_element.replace("Puntuación: ", "").replace(",", "."))
    except:
        review_mark = 0.0

    try:
        comment_amount_element = \
        hotel.find_element(By.CSS_SELECTOR, "div.abf093bdfe.f45d8e4c32.d935416c47").text.split(" ")[0]
        comment_amount = int(comment_amount_element.replace(".", ""))
    except:
        comment_amount = 0

    photo_urls = []
    try:
        photo_element = hotel.find_element(By.CSS_SELECTOR, 'img[data-testid="image"]')  # Adjust CSS selector
        photo_url = photo_element.get_attribute('src')
        photo_urls.append(photo_url)
    except:
        pass
    try:
        description = hotel.find_element(By.CSS_SELECTOR, "div.abf093bdfe:not(.ecc6a9ed89)").text
    except:
        description = ""

    average_price = 0.0

    # Create a Booking object without saving it to the DB
    return BookingDto(
        name=name,
        location=location,
        average_price=average_price,
        description=description,
        review_mark=review_mark,
        number_of_comments=comment_amount,
        photo_urls=photo_urls,
        amenities=[]
    )


