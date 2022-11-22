from django.db import models
from django.contrib.auth.models import User



class County(models.Model):
    NBI = 'Nairobi'
    MSA = 'Mombasa'
    NKR = 'Nakuru'
    KSM = 'Kisumu'

    COUNTY_OPTIONS = [
        (NBI, 'Nairobi'),
        (NKR, 'Mombasa'),
         (NKR, 'Nakuru'),
        (KSM, 'Kisumu'),
    ]

    county = models.CharField(max_length=255, choices=COUNTY_OPTIONS, null=True)

    def __str__(self):
        return self.county
class Patient(models.Model):
    M = 'Male'
    F = 'Female'

    GENDER_CHOICES = [
        (M, 'Male'),
        (F, 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient', null=True)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=F)
    created_at = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now = True)
    # def __str__(self):
    #     return f'{self.username} '

    # class Meta:
    #     ordering = ['first_name', 'last_name']



class Doctor(models.Model):

    CARD ='Cardiologist'
    DERMA = 'Dermatologist'
    EMERGE =  'Emergency Specialist'
    ALLERGY = 'Allergy Specialist'
    ANAE = 'Anesthesiologist'
    COLON = 'COlon and Rectal Surgeon'
    NORMAL = 'Consultant'


    SPECIALIZATION_CHOICES = [
        (CARD, 'Cardiologist'),
        (DERMA, 'Dermatologist'),
        (EMERGE, 'Emergency Specialist'),
        (ALLERGY, 'Allergy Specialist'),
        (ANAE, 'Anesthesiologist'),
        (COLON, 'COlon and Rectal Surgeon'),
        (NORMAL, 'Consultant'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor', null=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=255)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True)
    specialization = models.CharField(max_length=50,choices=SPECIALIZATION_CHOICES , null=True)
    birth_date = models.DateField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}'

    # class Meta:
    #     ordering = ['first_name', 'last_name']

        
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE)


