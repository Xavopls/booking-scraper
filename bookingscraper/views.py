import logging
from .usecases import gethotel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models.booking import Booking
from .serializers import BookingSerializer, BookingDtoSerializer
from .services.scraper import scrape_booking_hotel

logger = logging.getLogger(__name__)


# GET /api/hotels/scrape
class ScrapeHotelsView(APIView):
    def get(self, request):
        try:
            hotel = gethotel.invoke(request.GET.get('name'))
            print(hotel)
            if not hotel:
                return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = BookingDtoSerializer(hotel)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# POST /api/hotels/
class CreateHotelView(generics.CreateAPIView):
    serializer_class = BookingSerializer


# GET /api/hotels/
class ListHotelsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

# GET /api/hotels/{id}/
class RetrieveHotelView(generics.RetrieveAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
