from django.urls import path

from .views import (
    SizeCompanyListAPIView,
    TypeCompanyListAPIView,
    ExperienceForVacanyListAPIView,
    WorkTypesListAPIView,
    RegisterCompany,
    CreateVacancyAPIView
)

urlpatterns = [
    path('size-company/', SizeCompanyListAPIView.as_view(), name='size-company'),
    path('type-company/', TypeCompanyListAPIView.as_view(), name='size-company'),
    path('experience-for-vacany/', ExperienceForVacanyListAPIView.as_view(), name='size-company'),
    path('work-types/', WorkTypesListAPIView.as_view(), name='size-company'),

    path('register/', RegisterCompany.as_view(), name='register-company'),
    path('create-vacancy/', CreateVacancyAPIView.as_view(), name='create-vacancy'),

]