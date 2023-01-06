from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import (
    Worker,
    Education,
    Education_level,
    Work_experience,
    Languages,
    Language_types,
    Skills,
    Driver_licenses
)

from .serializers import (
    WorkerRegisterSerializer,
    EducationLevelSerializer,
    LanguagesSerializer,
    LanguageTypesSerializer,
    SkillsSerializer,
    DriverLicensesSerializer,
    CreateEducationSerializer,
    CreateWorkExperienceSerializer,
    CreateLanguagesSerializer, 
    ListWorkerSerializer,
    RetrieveWorkerSerializer
)

from .permissions import IsWorkerUser 
from company.models import Vacancy



class ELListAPIView(ListAPIView):
    queryset = Education_level.objects.all()
    serializer_class = EducationLevelSerializer

class LanguageTypesListAPIView(ListAPIView):
    queryset = Language_types.objects.all()
    serializer_class = LanguageTypesSerializer

class SkillsListAPIView(ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class DLListAPIView(ListAPIView):
    queryset = Driver_licenses.objects.all()
    serializer_class = DriverLicensesSerializer

class RegisterAPIView(CreateAPIView):
    serializer_class = WorkerRegisterSerializer

class CreateEducation(CreateAPIView):
    serializer_class = CreateEducationSerializer
    permission_classes = (IsAuthenticated, IsWorkerUser)

    def perform_create(self, serializer):
        user = self.request.user
        worker = Worker.objects.get(user=user)
        serializer.save(worker=worker) 

class CreateWorkExperience(CreateAPIView):
    serializer_class = CreateWorkExperienceSerializer
    permission_classes = (IsAuthenticated, IsWorkerUser)

    def perform_create(self, serializer):
        user = self.request.user
        worker = Worker.objects.get(user=user)
        serializer.save(worker=worker) 


class CreateLanguages(CreateAPIView):
    serializer_class = CreateLanguagesSerializer
    permission_classes = (IsAuthenticated, IsWorkerUser)

    def perform_create(self, serializer):
        user = self.request.user
        worker = Worker.objects.get(user=user)
        serializer.save(worker=worker) 
 
 
class WorkerListRetrieveAPIView(ModelViewSet):
    queryset = Worker.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ListWorkerSerializer
        if self.action == 'retrieve':
            return RetrieveWorkerSerializer 
 