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

admin.site.register(Company)
admin.site.register(Size_company)
admin.site.register(Type_company)
admin.site.register(Vacancy)
admin.site.register(Experience_for_vacany)
admin.site.register(Work_types)
admin.site.register(Requirements)
admin.site.register(Tasks) 
admin.site.register(Conditions) 
admin.site.register(Tags) 
