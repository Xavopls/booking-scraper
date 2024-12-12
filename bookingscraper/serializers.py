from rest_framework import serializers

from .dtos.bookingdto import BookingDto
from .models.amenity import Amenity
from .models.booking import Booking

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name']

class BookingSerializer(serializers.ModelSerializer):
    amenities = serializers.SerializerMethodField()  # Manually handle amenities

    class Meta:
        model = Booking
        fields = ['id', 'name', 'location', 'average_price', 'description',
                  'review_mark', 'number_of_comments', 'photo_urls', 'amenities']

    def get_amenities(self, obj):
        # Manually return amenities if any
        return [amenity.name for amenity in obj.amenities.all()]


class BookingDtoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)
    average_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    description = serializers.CharField(required=False, allow_blank=True)
    review_mark = serializers.FloatField(default=0.0)
    number_of_comments = serializers.IntegerField(default=0)
    photo_urls = serializers.ListField(child=serializers.URLField(), required=False)
    amenities = serializers.ListField(child=serializers.CharField(max_length=255), required=False)

    def create(self, validated_data):
        # Manually create a BookingDto instance
        return BookingDto(**validated_data)

    def update(self, instance, validated_data):
        # Update an existing BookingDto instance (although you may not need this if you're not persisting to a DB)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        return instance