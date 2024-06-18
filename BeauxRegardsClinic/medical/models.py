# medical/models.py

from django.db import models


class MedicalStaff(models.Model):
    STAFF_ROLES = (
        ('Nurse', 'Nurse'),
        ('Receptionist', 'Receptionist'),
        ('Doctor', 'Doctor'),
        ('Specialist', 'Specialist'),
    )
    DEPARTMENTS = (
        ('Cardiology', 'Cardiology'),
        ('Endocrinology', 'Endocrinology'),
        ('General Medicine', 'General Medicine'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    staff_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=STAFF_ROLES)
    department = models.CharField(max_length=30, choices=DEPARTMENTS)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_hire = models.DateField()
    shift_timings = models.CharField(max_length=50)
    qualifications = models.TextField()
    years_of_experience = models.PositiveIntegerField()
    specializations = models.TextField()
    supervisor_id = models.CharField(max_length=10, blank=True, null=True)
    emergency_contact = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    profile_picture = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    languages_spoken = models.CharField(max_length=100)
    employee_number = models.CharField(max_length=20, unique=True)
    office_location = models.CharField(max_length=100)
    access_level = models.CharField(max_length=20)
    schedule = models.TextField(blank=True, null=True)
    certifications_and_licenses = models.TextField(blank=True, null=True)
    training_records = models.TextField(blank=True, null=True)
    medical_clearances = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Patient(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    patient_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    medical_history = models.TextField()
    current_treatment = models.TextField()
    assigned_doctor = models.ForeignKey(MedicalStaff, on_delete=models.SET_NULL, null=True)
    emergency_contact = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
