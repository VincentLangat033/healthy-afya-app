from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    M = 'Male'
    F = 'Female'

    GENDER_CHOICES = [
        (M, 'Male'),
        (F, 'Female'),
    ]
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    # slug = models.SlugField(default='-')
    age = models.IntegerField(blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=F)
    created_at = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile',null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']



class Doctor(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    slug = models.SlugField(default='-')
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']

        
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE)


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