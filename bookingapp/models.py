from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver



class County(models.Model):
    NBI = 'Nairobi'
    MSA = 'Mombasa'
    NKR = 'Nakuru'
    KSM = 'Kisumu'

    COUNTY_OPTIONS = [
        (NBI, 'Nairobi'),
        (MSA, 'Mombasa'),
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
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=255)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True)
    specialization = models.CharField(max_length=50,choices=SPECIALIZATION_CHOICES , null=True)
    biography = models.TextField(null=True, default='-')   
    birth_date = models.DateField(null=True, blank=True)
    has_schedule = models.BooleanField(default=False)
    last_update = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.first_name




        
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE)


class Appointment(models.Model):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    symptoms = models.TextField(null=True)
    appointment_date = models.DateField(null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=PENDING)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_info')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_info')

    def __str__(self):
        return f'Appointment {self.created_at}'


class Schedule(models.Model):
    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    ]

    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    monday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    tuesday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    wednesday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    thursday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    friday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    saturday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    sunday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)

    def __str__(self):
        return f'Schedule for {self.doctor.user.first_name}'


class RegisterDoctor(models.Model):
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

    STATUS_PENDING = 'Pending'
    STATUS_APPROVED = 'Approved'
    STATUS_REJECTED = 'Rejected'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_registration')
    specialization = models.CharField(max_length=50,choices=SPECIALIZATION_CHOICES)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    biography = models.TextField(null=True, default='-')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_PENDING)

    def __str__(self):
        return f'Application for {self.user.first_name}'

    def save(self, *args, **kwargs):
        if self.status == 'Approved':
            doctor_data = Doctor.objects.create(user=self.user, specialization=self.specialization, county=self.county, biography=self.biography)
            doctor_data.save()
            group = Group.objects.get(id=1)
            group.user_set.add(self.user)
            email_header = f'Your application #{self.id} has been Approved'
            email_body = f'Dear Mr/Mrs {self.user.first_name} \n\n Congratulations! your application for being a doctor in afya healthcare has been approved! Kindly log in to set up your account. \n\n Regards,\n Afya Healthcare'
            # applicationEmail(self.user.email, email_header, email_body)
        elif self.status == 'Rejected':
            email_header = f'Your application #{self.id} has been Rejected'
            email_body = f'Dear Mr/Mrs {self.user.first_name} \n\n Unfortunately, your application for being a doctor has been rejected. If you still wish to to join us, you can reapply after 3 months. \n\n Regards,\n Afya Healthcare'
            # applicationEmail(self.user.email, email_header, email_body)
            return super().delete(*args, **kwargs)
        return super().save(*args, **kwargs)