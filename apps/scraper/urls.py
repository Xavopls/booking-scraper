
from django.urls import path

from apps.scraper.views.booking_views import BookingView, HotelView, HotelByIdView

urlpatterns = [

    path(r'scrape', BookingView.as_view(), name='scrape_hotels'),
    path('', HotelView.as_view(), name='create_hotel'),
    path('<int:booking_id>', HotelByIdView.as_view(), name='hotel_by_id')

]



