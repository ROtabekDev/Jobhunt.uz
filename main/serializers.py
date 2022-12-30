from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

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

class RegionSerializer(ModelSerializer):
    
    class Meta:
        model = Region
        fields = ('id', 'name')


class DistrictSerializer(ModelSerializer):
    region_id = serializers.StringRelatedField()

    class Meta:
        model = District
        fields = ('id', 'name', 'region_id')