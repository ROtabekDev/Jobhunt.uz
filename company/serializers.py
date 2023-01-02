from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import (
    Company,
    Size_company,
    Type_company,
    Vacancy,
    Experience_for_vacany,
    Work_types,
    Requirements,
    Tasks,
    Conditions,
    Tags
)

from main.serializers import CustomUserSerializer
from main.models import CustomUser 

class SizeCompanySerializer(ModelSerializer):
    
    class Meta:
        model = Size_company
        fields = ('id', 'name')

class TypeCompanySerializer(ModelSerializer):
    
    class Meta:
        model = Type_company
        fields = ('id', 'name')

class ExperienceForVacanySerializer(ModelSerializer):
    
    class Meta:
        model = Experience_for_vacany
        fields = ('id', 'name')

class WorkTypesSerializer(ModelSerializer):
    
    class Meta:
        model = Work_types
        fields = ('id', 'name')

class RequirementsSerializer(ModelSerializer):
    
    class Meta:
        model = Requirements
        fields = ('id', 'name')

class TasksSerializer(ModelSerializer):
    
    class Meta:
        model = Tasks
        fields = ('id', 'name')

class ConditionsSerializer(ModelSerializer):
    
    class Meta:
        model = Conditions
        fields = ('id', 'name')

class TagsSerializer(ModelSerializer):
    
    class Meta:
        model = Tags
        fields = ('id', 'name')


class CompanyRegisterSerializer(ModelSerializer):
    user = CustomUserSerializer() 
    
    class Meta:
        model = Company
        fields = ('user','name_company', 'legal_name_company', 'industrial_sector', 'speciality', 'size_company', 'type_company', 'description', 'web_page')
     
    def create(self, validated_data): 
        user = dict(validated_data.pop('user'))  
        del user['password2'] 
        user = CustomUser.objects.create_user(
                                        phone_number=user['phone_number'],
                                        email=user['email'],
                                        region_id=user['region_id'],
                                        district_id=user['district_id'],
                                        password=user['password']
                                        )
        
        industrial_sector = validated_data.pop('industrial_sector')                        
        speciality = validated_data.pop('speciality')   

        instance = Company.objects.create(
            user=user,
            **validated_data
            )
        instance.industrial_sector.set(industrial_sector)
        instance.speciality.set(speciality)
        return instance