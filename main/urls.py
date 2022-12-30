from django.urls import path

from .views import (
    RegionListAPIView,
    DistrictListAPIView
)

urlpatterns = [
    path('regions/', RegionListAPIView.as_view(), name='regions'),
    path('districts/', DistrictListAPIView.as_view(), name='districts'),
]