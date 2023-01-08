from django.urls import path

from .views import (
    RegisterAPIView,
    WorkerListRetrieveAPIView,
    WorkerProfile, 
    ELListAPIView,
    LanguageTypesListAPIView,
    SkillsListAPIView,
    DLListAPIView,
    CreateEducation,
    CreateWorkExperience,
    CreateLanguages
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register-worker'),
    
    path('candidate/', WorkerListRetrieveAPIView.as_view({'get': 'list'})),
    path('candidate/<int:pk>/', WorkerListRetrieveAPIView.as_view({'get': 'retrieve'})),  
    
    path('profile/', WorkerProfile.as_view()),
 
    path('education-level/', ELListAPIView.as_view(), name='education-level'),
    path('language-types/', LanguageTypesListAPIView.as_view(), name='language-types'),
    path('skills/', SkillsListAPIView.as_view(), name='skills'),
    path('driver-licenses/', DLListAPIView.as_view(), name='driver-licenses'),

    path('create-education/', CreateEducation.as_view(), name='create-education'),
    path('create-work-experience/', CreateWorkExperience.as_view(), name='create-work-experience'),
    path('create-languages/', CreateLanguages.as_view(), name='create-languages'),
]