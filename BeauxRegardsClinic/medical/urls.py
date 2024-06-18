# medical/urls.py

from django.urls import path, include
# medical/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicalStaffViewSet, PatientViewSet, UserCreateView

router = DefaultRouter()
router.register(r'medicalstaff', MedicalStaffViewSet)
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreateView.as_view(), name='user-register'),
]
