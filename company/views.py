from rest_framework.generics import ListAPIView

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

from .serializers import (
    SizeCompanySerializer,
    TypeCompanySerializer,
    ExperienceForVacanySerializer,
    WorkTypesSerializer 
)

class SizeCompanyListAPIView(ListAPIView):
    queryset = Size_company.objects.all()
    serializer_class = SizeCompanySerializer

class TypeCompanyListAPIView(ListAPIView):
    queryset = Type_company.objects.all()
    serializer_class = TypeCompanySerializer

class ExperienceForVacanyListAPIView(ListAPIView):
    queryset = Experience_for_vacany.objects.all()
    serializer_class = ExperienceForVacanySerializer

class WorkTypesListAPIView(ListAPIView):
    queryset = Work_types.objects.all()
    serializer_class = WorkTypesSerializer