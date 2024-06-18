from django.contrib import admin
from .models import MedicalStaff, Patient

@admin.register(MedicalStaff)
class MedicalStaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'first_name', 'last_name', 'role', 'department', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'department')
    list_filter = ('role', 'department', 'status')
    ordering = ('staff_id',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'first_name', 'last_name', 'email', 'assigned_doctor')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('gender', 'assigned_doctor')
    ordering = ('patient_id',)