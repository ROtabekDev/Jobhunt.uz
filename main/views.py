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
    DistrictSerializer
)


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
 
class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filterset_fields = ['region_id']