from django.urls import path

from .views import (
    RegionListAPIView,
    DistrictListAPIView,
    SNTypesListAPIView,
    CurrencyTypesListAPIView,
    IndisturialSectorListAPIView,
    SpecialityListAPIView
)

urlpatterns = [
    path('regions/', RegionListAPIView.as_view(), name='regions'),        # api/v1/main/regions/
    path('districts/', DistrictListAPIView.as_view(), name='districts'),  # api/v1/main/districts/?region_id=pk
    path('sntypes/', SNTypesListAPIView.as_view(), name='social_network_types'), # api/v1/main/sntypes/
    path('currency-types/', CurrencyTypesListAPIView.as_view(), name='currency-types'), # api/v1/main/currency-types/
    path('indisturial-sectors/', IndisturialSectorListAPIView.as_view(), name='ndisturial-sectors'), # api/v1/main/indisturial-sectors/
    path('speciality/', SpecialityListAPIView.as_view(), name='speciality'), # api/v1/main/speciality/
]