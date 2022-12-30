from rest_framework.generics import ListAPIView

from .models import (
    CustomUser,
    Region,
    District,
    Social_networks,
    Social_network_types,
    Indisturial_sector,
    Speciality,
    Currency_types
)

from .serializers import (
    RegionSerializer,
    DistrictSerializer,
    SNTypesSerializer,
    CurrencyTypesSerializer,
    IndisturialSectorSerializer,
    SpecialitySerializer
)


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
 
class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filterset_fields = ['region_id']

class SNTypesListAPIView(ListAPIView):
    queryset = Social_network_types.objects.all()
    serializer_class = SNTypesSerializer

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