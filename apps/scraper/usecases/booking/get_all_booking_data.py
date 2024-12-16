from apps.core.models import Booking
from apps.core.serializers.booking_serializer import BookingSerializer
from apps.core.services.utils import UtilsService
from apps.scraper.service.booking_scraper_service import BookingScraperService
from apps.scraper.service.selenium_service import SeleniumService


class GetAllBookingData:
    def invoke(self):
        try:
            booking = Booking.objects.all()
            return booking

        except Exception as e:
            # Log the exception and return a False or an error message
            print(f"Error retrieving booking data: {e}")
            return False