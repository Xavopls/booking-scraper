from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.scraper.usecases.booking.get_booking_data import GetBookingData
from apps.core.serializers.booking_serializer import BookingSerializer
from rest_framework.views import APIView

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
class CreateHotelView(CreateAPIView):
    @extend_schema(
        request=BookingSerializer
    )
    def post(self, request):
        # Initialize the serializer with the request data
        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():
            # Extract the validated data
            booking_data = serializer.validated_data

            # Create an instance of UploadBookingData and call invoke
            upload_service = UploadBookingData()
            success = upload_service.invoke(booking_data)

            if success:
                return Response({"message": "Booking uploaded successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Failed to upload booking."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#
#
# # GET /api/hotels/
# class ListHotelsView(generics.ListAPIView):
#     serializer_class = BookingSerializer
#     queryset = Booking.objects.all()
#
#
# # GET /api/hotels/{id}/
# class RetrieveHotelView(generics.RetrieveAPIView):
#     serializer_class = BookingSerializer
#     queryset = Booking.objects.all()
