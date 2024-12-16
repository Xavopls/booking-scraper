# services.py (or any other appropriate location for your service classes)
from apps.core.models import Booking
from apps.core.serializers.booking_serializer import BookingSerializer
import logging

logger = logging.getLogger(__name__)

class UploadBookingData:
    def invoke(self, booking_data: BookingSerializer):
        try:
            booking_data.save()
            return True
        except Exception as e:
            # Catch any other exceptions that might occur
            logger.error(f"An unexpected error occurred: {str(e)}")
            return {"error": "An unexpected error occurred while saving the booking."}
