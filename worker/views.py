from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

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
    CreateEducationSerializer
)

from .permissions import IsWorkerUser

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

