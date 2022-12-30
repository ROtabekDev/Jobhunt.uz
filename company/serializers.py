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