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

from django.core.exceptions import ObjectDoesNotExist
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

        company = Company.objects.create(
            user=user,
            **validated_data
            )
        company.industrial_sector.set(industrial_sector)
        company.speciality.set(speciality)
        return company

class CreateVacancySerializer(ModelSerializer):
    company = serializers.StringRelatedField(read_only=True) 
    requirements = RequirementsSerializer(write_only=True, many=True)
    tasks = RequirementsSerializer(write_only=True, many=True)
    conditions = RequirementsSerializer(write_only=True, many=True)
    tags = RequirementsSerializer(write_only=True, many=True)


    class Meta:
        model = Vacancy
        fields = (
            'company', 
            'industrial_sector',
            'title',
            'work_experience',
            'type_work',
            'salary_type',
            'currency_type',
            'start_salary',
            'end_salary',
            'is_online',
            'region',
            'district',
            'requirements',
            'tasks',
            'conditions',
            'tags'
            )

    def create(self, validated_data):   
        requirements = validated_data.pop('requirements')   
        tasks = validated_data.pop('tasks')   
        conditions = validated_data.pop('conditions')   
        tags = validated_data.pop('tags')   
 
        vacancy = Vacancy.objects.create( 
            **validated_data
            ) 
            
        for requirement in requirements:
            try:
                talab = Requirements.objects.get(name=requirement['name'])
                vacancy.requirements.remove(talab)
                vacancy.requirements.add(talab) 
            except ObjectDoesNotExist:  
                talab = Requirements.objects.create(name=requirement['name'])
                vacancy.requirements.add(talab) 

        for task in tasks:
            try:
                vazifa = Tasks.objects.get(name=task['name'])
                vacancy.tasks.remove(vazifa)
                vacancy.tasks.add(vazifa) 
            except ObjectDoesNotExist: 
                vazifa = Tasks.objects.create(name=task['name'])
                vacancy.tasks.add(vazifa) 

        for condition in conditions:
            try:  
                shart = Conditions.objects.get(name=condition['name'])
                vacancy.conditions.remove(shart)
                vacancy.conditions.add(shart) 
            except ObjectDoesNotExist:  
                shart = Conditions.objects.create(name=condition['name'])
                vacancy.conditions.add(shart) 

        for tag in tags: 
            try:  
                teg = Tags.objects.get(name=tag['name'])
                vacancy.tags.remove(teg)
                vacancy.tags.add(teg) 
            except ObjectDoesNotExist:  
                teg = Tags.objects.create(name=tag['name'])
                vacancy.tags.add(teg)  
                
        return vacancy