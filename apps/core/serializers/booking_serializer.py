# apps/scraper/serializers/booking_serializer.py

from rest_framework import serializers
from apps.core.models.booking import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',
            'name',
            'location',
            'average_price',
            'description',
            'review_mark',
            'number_of_comments',
            'photo_urls',
            'amenities',
        ]

    def create(self, validated_data):
        # Extract amenities from validated_data
        amenities = validated_data.pop('amenities', [])

        # Create Booking instance
        booking = Booking.objects.create(**validated_data)

        # Set many-to-many relationships
        booking.amenities.set(amenities)

        return booking
