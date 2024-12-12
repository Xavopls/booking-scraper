from django.db import models
from .amenity import Amenity


class Booking(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    average_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    review_mark = models.FloatField()
    number_of_comments = models.IntegerField()
    photo_urls = models.JSONField(default=list)
    amenities = models.ManyToManyField(Amenity, blank=True)

    def __str__(self):
        return self.name

