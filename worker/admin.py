from django.contrib import admin

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
 
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'gender', 'birthday') 
    list_display_links = ('user',  'full_name') 

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'speciality', 'education_leval') 
    list_display_links = ('place_name',  'speciality', 'education_leval') 

@admin.register(Education_level)
class EducationLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 

@admin.register(Work_experience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'company_name') 
    list_display_links = ('position',  'company_name') 

@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'language_type', 'level') 
    list_display_links = ('language_type',  'level') 

@admin.register(Language_types)
class LanguageTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 

@admin.register(Driver_licenses)
class DriverLicensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 