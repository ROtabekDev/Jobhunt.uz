from django.contrib import admin

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

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name_company') 
    list_display_links = ('user', 'name_company') 

@admin.register(Size_company)
class SizeCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 

@admin.register(Type_company)
class TypeCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 

@admin.register(Vacancy)
class EVacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'industrial_sector', 'title', 'work_experience') 
    list_display_links = ('industrial_sector', 'title') 

@admin.register(Experience_for_vacany)
class ExperienceForVacanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 

@admin.register(Work_types)
class WorkTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 

@admin.register(Requirements)
class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 

@admin.register(Conditions)
class ConditionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 
