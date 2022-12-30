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

class SNTypesSerializer(ModelSerializer):

    class Meta:
        model = Social_network_types
        fields = ('id', 'name')

class SocialNetworksSerializer(ModelSerializer):
    social_network_id = serializers.StringRelatedField()

    class Meta:
        model = Social_networks
        fields = ('id', 'social_network_id', 'nickname')

class CurrencyTypesSerializer(ModelSerializer):

    class Meta:
        model = Currency_types
        fields = ('id', 'name')

class IndisturialSectorSerializer(ModelSerializer):

    class Meta:
        model = Indisturial_sector
        fields = ('id', 'name')


class SpecialitySerializer(ModelSerializer):
    idustrial_sector_id = serializers.StringRelatedField()

    class Meta:
        model = Speciality
        fields = ('id', 'name', 'idustrial_sector_id', 'for_worker')