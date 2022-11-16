from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import  messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from .models import Patient


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            birth_date = form.cleaned_data.get('birth_date')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = User.objects.get(username=username, password=password)
            user_data = Patient.objects.create(user=user, phone=phone, gender=gender, birth_date=birth_date, first_name=first_name, last_name=last_name)
            user_data.save()

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration succesful"))
            return redirect('home')

    else:
        form = RegisterUserForm()
    return render(request,'home/register_patient.html', {'form': form} )

def home(request):
    return render(request, 'home/index.html')

