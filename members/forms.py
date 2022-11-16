from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


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
        fields = ('username', 'phone', 'gender', 'birth_date' 'first_name', 'last_name', 'email', 'password1', 'password2')
