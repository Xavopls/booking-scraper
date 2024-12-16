from django.http import Http404
from rest_framework.generics import get_object_or_404

from apps.core.models import Booking
from apps.core.serializers.booking_serializer import BookingSerializer
from apps.core.services.utils import UtilsService
from apps.scraper.service.booking_scraper_service import BookingScraperService
from apps.scraper.service.selenium_service import SeleniumService


class GetBookingDataById:
    def invoke(self, booking_id: int):
        try:
            return Booking.objects.get(id=booking_id)
        except:
            return False

