from django.urls import path

from .views import (
    RegisterCompany,
    CompanyListAPIView,
    CompanyRetrieveAPIView,
    CompanyProfile,
    CreateVacancyAPIView,
    VacancyListAPIView,
    VacancyRetrieveAPIView,
    SizeCompanyListAPIView,
    TypeCompanyListAPIView,
    ExperienceForVacanyListAPIView,
    WorkTypesListAPIView,
)

urlpatterns = [ 
    path('register/', RegisterCompany.as_view(), name='register-company'),
    path('profile/', CompanyProfile.as_view()),
    path('company-list/', CompanyListAPIView.as_view()),
    path('company-list/<int:pk>/', CompanyRetrieveAPIView.as_view()), 
  
    path('vacancy/', VacancyListAPIView.as_view()),
    path('vacancy/<int:pk>/', VacancyRetrieveAPIView.as_view()), 
    path('create-vacancy/', CreateVacancyAPIView.as_view(), name='create-vacancy'),
  
    path('size-company/', SizeCompanyListAPIView.as_view(), name='size-company'),
    path('type-company/', TypeCompanyListAPIView.as_view(), name='size-company'),
    path('experience-for-vacany/', ExperienceForVacanyListAPIView.as_view(), name='size-company'),
    path('work-types/', WorkTypesListAPIView.as_view(), name='size-company'),
]