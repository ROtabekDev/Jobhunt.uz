from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import (
    Worker,
    Education,
    Education_level,
    Work_experience,
    Languages,
    Language_types,
    Skills,
    Driver_licenses
)


class EducationLevelSerializer(ModelSerializer):

    class Meta:
        model = Education_level
        fields = ('id', 'name')

class LanguagesSerializer(ModelSerializer):
    language_type = serializers.StringRelatedField()

    class Meta:
        model = Languages
        fields = ('id', 'language_type', 'leval')

class LanguageTypesSerializer(ModelSerializer):

    class Meta:
        model = Language_types
        fields = ('id', 'name')

class SkillsSerializer(ModelSerializer):

    class Meta:
        model = Skills
        fields = ('id', 'name')

class DriverLicensesSerializer(ModelSerializer):

    class Meta:
        model = Driver_licenses
        fields = ('id', 'name')