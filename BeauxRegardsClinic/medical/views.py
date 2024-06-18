# medical/views.py

# medical/views.py

from rest_framework import generics
from django.contrib.auth.models import User
from .serializers_ import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import MedicalStaff, Patient
from .serializers_ import MedicalStaffSerializer, PatientSerializer

class MedicalStaffViewSet(viewsets.ModelViewSet):
    queryset = MedicalStaff.objects.all()
    serializer_class = MedicalStaffSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
