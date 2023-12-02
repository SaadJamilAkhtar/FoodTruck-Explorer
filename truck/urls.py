from django.urls import path
from .views import *

urlpatterns = [
    path("", FoodTruckListAPIView.as_view(), name='index'),
    path('upload-csv/', UploadCSVView.as_view(), name='upload-csv'),
]
