from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

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
    WorkTypesSerializer, 
    CompanyRegisterSerializer,
    CreateVacancySerializer,
)

from .permissions import IsCompanyUser

class RegisterCompany(CreateAPIView):
    serializer_class = CompanyRegisterSerializer

class CreateVacancyAPIView(CreateAPIView):
    serializer_class = CreateVacancySerializer 
    permission_classes = (IsAuthenticated, IsCompanyUser)  

    def perform_create(self, serializer):
        user = self.request.user
        company = Company.objects.get(user=user)
        serializer.save(company=company) 
    
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