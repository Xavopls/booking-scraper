# apps/scraper/serializers/booking_serializer.py

from rest_framework import serializers
from apps.core.models.booking import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking

        fields = ['id',
                  'name',
                  'location',
                  'average_price',
                  'description',
                  'review_mark',
                  'number_of_comments',
                  'photo_urls',
                  'amenities']

    def to_domain(self):
        booking = Booking.objects.create(
            id=self.context['id'],
            name=self.context['name'],
            location=self.context['location'],
            average_price=self.context['average_price'],
            description=self.context['description'],
            review_mark=self.context['review_mark'],
            number_of_comments=self.context['number_of_comments'],
            photo_urls=self.context['photo_urls'],
            amenities=self.context['amenities']
        )

        return booking
