from django.urls import path

from .views import (
    ELListAPIView,
    LanguageTypesListAPIView,
    SkillsListAPIView,
    DLListAPIView,
    RegisterAPIView
)

urlpatterns = [
    path('education-level/', ELListAPIView.as_view(), name='education-level'),
    path('language-types/', LanguageTypesListAPIView.as_view(), name='language-types'),
    path('skills/', SkillsListAPIView.as_view(), name='skills'),
    path('driver-licenses/', DLListAPIView.as_view(), name='driver-licenses'),

    path('register/', RegisterAPIView.as_view(), name='register-worker'),
]