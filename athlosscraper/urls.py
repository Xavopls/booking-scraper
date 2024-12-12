"""
URL configuration for athlosscraper project.

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
from django.contrib import admin
from django.urls import path
from bookingscraper.views import ScrapeHotelsView, CreateHotelView, ListHotelsView, RetrieveHotelView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hotels/scrape', ScrapeHotelsView.as_view(), name='scrape-hotels'),
    path('api/hotels/', CreateHotelView.as_view(), name='create-hotel'),
    path('api/hotels/all', ListHotelsView.as_view(), name='list-hotels'),
    path('api/hotels/<int:pk>/', RetrieveHotelView.as_view(), name='retrieve-hotel'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
