from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from rest_framework.exceptions import AuthenticationFailed 
from django.contrib.auth import authenticate

from .models import (
    CustomUser,
    Region,
    District, 
    Indisturial_sector,
    Speciality,
    Currency_types
)

from worker.models import Worker
from company.models import Company

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
 
class LoginSerializer(serializers.ModelSerializer): 
    phone_number = serializers.CharField(max_length=15) 
    password = serializers.CharField(max_length=68, min_length=6, write_only=True) 
    token = serializers.DictField(source='tokens', read_only=True)  
    worker_user = serializers.DictField(read_only=True)
    company_user = serializers.DictField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('phone_number', 'password', 'token', 'worker_user', 'company_user')

    def validate(self, attrs):  
        phone_number = attrs.get('phone_number', '')
        password = attrs.get('password', '') 

        user = authenticate(phone_number=phone_number, password=password) 
        
 
        if not user:
            raise AuthenticationFailed({
                'message': 'Telefon nomer yoki parol noto`g`ri yoki foydalanuvchi faol emas.'
            })   

        worker_user = Worker.objects.filter(user=user) 
        company_user = Company.objects.filter(user=user) 

        if worker_user.exists(): 
            return { 
                'worker_user': worker_user.values()[0], 
                'phone_number': user.phone_number, 
                'tokens': user.tokens
            }
        elif company_user.exists(): 
            return {  
                'company_user': company_user.values()[0], 
                'phone_number': user.phone_number,  
                'tokens': user.tokens
            }
        return {  
            'phone_number': user.phone_number, 
            'tokens': user.tokens
        } 

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
