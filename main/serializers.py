from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import (
    CustomUser,
    Region,
    District, 
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

class CustomUserSerializer(ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.DictField(source='tokens', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'phone_number', 'email',  'region_id', 'district_id', 'password', 'password2', 'token')
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError({'success': False, 'message': 'Parollar bir xil emas.'})
        return attrs
 