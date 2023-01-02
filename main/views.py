from rest_framework.generics import ListAPIView, CreateAPIView

from .models import ( 
    Region,
    District, 
    Indisturial_sector,
    Speciality,
    Currency_types
)

from .serializers import (
    RegionSerializer,
    DistrictSerializer, 
    CurrencyTypesSerializer,
    IndisturialSectorSerializer,
    SpecialitySerializer,
    LoginSerializer
) 

class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer

    def perform_create(self, serializer):
        pass

class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
 
class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filterset_fields = ['region_id'] 

class CurrencyTypesListAPIView(ListAPIView):
    queryset = Currency_types.objects.all()
    serializer_class = CurrencyTypesSerializer

class IndisturialSectorListAPIView(ListAPIView):
    queryset = Indisturial_sector.objects.all()
    serializer_class = IndisturialSectorSerializer

class SpecialityListAPIView(ListAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    filterset_fields = ['for_worker']