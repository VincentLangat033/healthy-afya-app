from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import *


class RegisterUserForm(UserCreationForm):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    YEARS= [x for x in range(1940,2021)]
    phone = forms.CharField(required=True)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    gender = forms.CharField(label='Choose your Gender', widget=forms.Select(choices=GENDER_CHOICES), required=True)
    birth_date = forms.DateField(label='Enter your birth details', widget=forms.SelectDateWidget(years=YEARS), required=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'gender', 'birth_date', 'first_name', 'last_name', 'email', 'password1', 'password2')


class RegisterDoctorForm(UserCreationForm):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    YEARS= [x for x in range(1940,2021)]
    phone = forms.CharField(required=True)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    gender = forms.CharField(label='Choose your Gender', widget=forms.Select(choices=GENDER_CHOICES), required=True)
    birth_date = forms.DateField(label='Enter your birth details', widget=forms.SelectDateWidget(years=YEARS), required=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'gender', 'birth_date', 'first_name', 'last_name', 'email', 'password1', 'password2')



class BookAppointmentForm(ModelForm):
    appointment_date = forms.CharField(widget=forms.TextInput(attrs={'id':'appointment_date', 'class': 'input-field', 'placeholder': 'Enter Date', 'autocomplete': 'off'}), required=True)
    symptoms = forms.Textarea()

    class Meta:
        model = Appointment
        fields = ['appointment_date', 'symptoms']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['symptoms'].widget.attrs.update({'class': 'input-field', 'cols': '30', 'rows': '10'})


class CreateScheduleForm(ModelForm):
    STATUS_CHOICE = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    ]

    monday = forms.CharField(label='Monday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    tuesday = forms.CharField(label='Tuesday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    wednesday = forms.CharField(label='Wednesday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    thursday = forms.CharField(label='Thursday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    friday = forms.CharField(label='Friday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    saturday = forms.CharField(label='Saturday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    sunday = forms.CharField(label='Sunday', widget=forms.Select(choices=STATUS_CHOICE), required=True)

    class Meta:
        model = Schedule
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['monday'].widget.attrs.update({'class': 'input-field'})
        self.fields['tuesday'].widget.attrs.update({'class': 'input-field'})
        self.fields['wednesday'].widget.attrs.update({'class': 'input-field'})
        self.fields['thursday'].widget.attrs.update({'class': 'input-field'})
        self.fields['friday'].widget.attrs.update({'class': 'input-field'})
        self.fields['saturday'].widget.attrs.update({'class': 'input-field'})
        self.fields['sunday'].widget.attrs.update({'class': 'input-field'})



class ApproveAppointmentForm(ModelForm):
    STATUS_CHOICE = [
        ('Approved', 'Approved'),
    ]
    YEARS= [x for x in range(2022,2040)]

    appointment_date = forms.CharField(widget=forms.TextInput(attrs={'id':'appointment_date', 'class': 'input-field', 'autocomplete': 'off'}), required=True)
    status = forms.CharField(label='Status', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'status']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'input-field'})

class RejectAppointmentForm(ModelForm):
    STATUS_CHOICE = [
        ('Rejected', 'Rejected')
    ]

    status = forms.CharField(label='Status', widget=forms.Select(choices=STATUS_CHOICE), required=True)

    class Meta:
        model = Appointment
        fields = ['status']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'input-field'})


class DoctorApplicationForm(ModelForm):
    SPECIALIZATION_CHOICES = [
        ('Cardiologist', 'CARD'),
        ('DERMA', 'Dermatologist'),
        ('EMERGE', 'Emergency Specialist'),
        ('ALLERGY', 'Allergy Specialist'),
        ('ANAE', 'Anesthesiologist'),
        ('COLON', 'COlon and Rectal Surgeon'),
        ('NORMAL', 'Consultant'),
    ]

    STATUS_CHOICE = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    specialization = forms.CharField(label='Choose Specialization', widget=forms.Select(choices=SPECIALIZATION_CHOICES), required=True)
    biography = forms.Textarea()

    class Meta:
        model = RegisterDoctor
        fields = ['specialization', 'county', 'biography']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specialization'].widget.attrs.update({'class': 'input-field'})
        self.fields['county'].widget.attrs.update({'class': 'input-field',})
        self.fields['biography'].widget.attrs.update({'class': 'input-field', 'cols': '30', 'rows': '10'})