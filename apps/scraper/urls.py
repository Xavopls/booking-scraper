
"""
URL configuration for athlos_tech_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from apps.scraper.views.booking_views import BookingView, CreateHotelView

urlpatterns = [

    path(r'scrape', BookingView.as_view(), name='scrape_hotels'),
    path('', CreateHotelView.as_view(), name='scrape_hotels'),

    # path('api/hotels/', CreateHotelView.as_view(), name='create-hotel'),
    # path('api/hotels/all', ListHotelsView.as_view(), name='list-hotels'),
    # path('api/hotels/<int:pk>/', RetrieveHotelView.as_view(), name='retrieve-hotel'),

]



