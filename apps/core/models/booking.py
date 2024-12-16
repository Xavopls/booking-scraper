from django.db import models
from .amenity import Amenity


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    average_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    review_mark = models.FloatField(null=True, blank=True)
    number_of_comments = models.IntegerField(null=True, blank=True)
    photo_urls = models.JSONField(default=list, null=True, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)

    def __str__(self):
        return self.name

