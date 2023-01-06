import json
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

from main.models import CustomUser
from main.serializers import CustomUserSerializer

from company.models import Vacancy
from company import serializers as company_serializers


class ListVacancySerializer(ModelSerializer):
    company = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    district = serializers.StringRelatedField() 

    class Meta:
        model = Vacancy
        fields = ('id','title', 'company', 'start_salary', 'end_salary', 'region', 'district')

class RetrieveVacancySerializer(ModelSerializer):
    company = serializers.StringRelatedField() 
    work_experience = serializers.StringRelatedField()
    type_work = serializers.StringRelatedField()
    currency_type = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    district = serializers.StringRelatedField()
    requirements = company_serializers.RequirementsSerializer(read_only=True, many=True)
    tasks = company_serializers.TasksSerializer(read_only=True, many=True)
    conditions = company_serializers.ConditionsSerializer(read_only=True, many=True)
    tags = company_serializers.TagsSerializer(read_only=True, many=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'company', 'title', 'work_experience', 'type_work', 'salary_type', 'currency_type', 'start_salary', 'end_salary', 'is_online', 'region', 'district', 'requirements', 'tasks', 'conditions', 'tags')

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


class WorkerRegisterSerializer(ModelSerializer):
    user = CustomUserSerializer() 
    
    class Meta:
        model = Worker
        fields = ('user','full_name', 'gender', 'birthday', 'industurial_sector_id', 'specility_id', 'salary', 'currency_type_id', 'skills', 'driver_license', 'is_freelancer')
     
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
        
        skills = validated_data.pop('skills')                        
        driver_license = validated_data.pop('driver_license')   

        worker = Worker.objects.create(
            user=user,
            **validated_data
            )
        worker.skills.set(skills)
        worker.driver_license.set(driver_license)
        return worker

class CreateEducationSerializer(ModelSerializer):
    worker = serializers.StringRelatedField()

    class Meta:
        model = Education
        fields = ('worker','place_name', 'education_leval', 'speciality', 'start_month', 'start_year', 'is_active', 'end_month', 'end_year', 'description')

    def create(self, validated_data):  
        worker = validated_data.get('worker') 

        education = Education.objects.create( 
            **validated_data
            )
        worker.education.add(education) 
        return education

class CreateWorkExperienceSerializer(ModelSerializer):
    worker = serializers.StringRelatedField()

    class Meta:
        model = Work_experience
        fields = ('worker','position', 'company_name', 'start_month', 'start_year', 'is_active', 'end_month', 'end_year', 'description')

    def create(self, validated_data):  
        worker = validated_data.get('worker') 

        work_experience = Work_experience.objects.create( 
            **validated_data
            )
        worker.work_experience.add(work_experience) 
        return work_experience

class CreateLanguagesSerializer(ModelSerializer):
    worker = serializers.StringRelatedField()

    class Meta:
        model = Languages
        fields = ('worker','language_type', 'level')

    def create(self, validated_data):  
        worker = validated_data.get('worker') 

        language = Languages.objects.create( 
            **validated_data
            )
        worker.languages.add(language) 
        return language