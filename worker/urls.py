from django.urls import path

from .views import (
    ELListAPIView,
    LanguageTypesListAPIView,
    SkillsListAPIView,
    DLListAPIView,
    RegisterAPIView,
    CreateEducation,
    CreateWorkExperience,
    CreateLanguages,
    WorkerListRetrieveAPIView,
    WorkerProfile
 
)

urlpatterns = [
    path('education-level/', ELListAPIView.as_view(), name='education-level'),
    path('language-types/', LanguageTypesListAPIView.as_view(), name='language-types'),
    path('skills/', SkillsListAPIView.as_view(), name='skills'),
    path('driver-licenses/', DLListAPIView.as_view(), name='driver-licenses'),

    path('register/', RegisterAPIView.as_view(), name='register-worker'),
    path('create-education/', CreateEducation.as_view(), name='create-education'),
    path('create-work-experience/', CreateWorkExperience.as_view(), name='create-work-experience'),
    path('create-languages/', CreateLanguages.as_view(), name='create-languages'),

    
    path('candidate/', WorkerListRetrieveAPIView.as_view({'get': 'list'})),
    path('candidate/<int:pk>/', WorkerListRetrieveAPIView.as_view({'get': 'retrieve'})),  
    
    path('profile/', WorkerProfile.as_view()),
]