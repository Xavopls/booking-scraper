from django.http import Http404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.scraper.usecases.booking.get_all_booking_data import GetAllBookingData
from apps.scraper.usecases.booking.get_booking_data import GetBookingData
from apps.core.serializers.booking_serializer import BookingSerializer
from rest_framework.views import APIView

from apps.scraper.usecases.booking.get_booking_data_by_id import GetBookingDataById
from apps.scraper.usecases.booking.upload_booking_data import UploadBookingData


# GET /api/hotels/scrape
class BookingView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter("name", OpenApiTypes.STR, OpenApiParameter.QUERY),
        ],
        responses=BookingSerializer,
    )
    def get(self, request):
        name = request.GET.get('name')
        if not name:
            return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            get_booking_data = GetBookingData()
            booking_data = get_booking_data.invoke(name)

            if not booking_data:
                return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = BookingSerializer(booking_data)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# POST /api/hotels/
class HotelView(CreateAPIView):
    @extend_schema(
        responses=BookingSerializer,
    )
    def get(self, request):
        try:
            get_all_booking_data = GetAllBookingData()
            bookings = get_all_booking_data.invoke()
            if not bookings:
                return Response({"message": "Booking not found."},
                                status=status.HTTP_404_NOT_FOUND)

            serializer = BookingSerializer(bookings, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Failed to retrieve bookings."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=BookingSerializer
    )
    def post(self, request):
        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():
            upload_service = UploadBookingData()
            success = upload_service.invoke(serializer)

            if success:
                return Response({"message": "Booking uploaded successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Failed to upload booking."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print(serializer.errors)  # Or use logging
            return Response({"message": "Validation failed", "errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
#
class HotelByIdView(ListAPIView):
    @extend_schema(
        responses=BookingSerializer,
    )
    def get(self, request, booking_id):
        try:
            get_booking_data_by_id = GetBookingDataById()
            booking = get_booking_data_by_id.invoke(booking_id)
            if not booking:
                return Response({"message": f"Booking with ID {booking_id} not found."},
                                status=status.HTTP_404_NOT_FOUND)

            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response({"message": "Failed to retrieve bookings."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
