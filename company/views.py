from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

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
    ListVacancySerializer,
    RetrieveVacancySerializer,
    ListCompanySerializer,
    RetrieveCompanySerializer
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

class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = ListVacancySerializer
    filterset_fields = ['region', 'district', 'industrial_sector']

class VacancyRetrieveAPIView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = RetrieveVacancySerializer

class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = ListCompanySerializer
    filterset_fields = ['industrial_sector']

class CompanyRetrieveAPIView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = RetrieveCompanySerializer 

class CompanyProfile(RetrieveUpdateAPIView):
    serializer_class = RetrieveCompanySerializer
    permission_classes = [IsAuthenticated, IsCompanyUser] 

    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj