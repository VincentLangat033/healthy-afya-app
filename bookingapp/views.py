from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import  messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, RegisterDoctorForm
from .models import Patient, County, Doctor, Appointment


@login_required(login_url='/members/login_user/')
def doctor_region(request):
    doctor_region = County.objects.all()
    return render(request, 'doctor/regions.html',{'doctor_region': doctor_region})

def patient_dashboard(request):
    return render(request, 'patient/dashboard.html')

def dashboard_content(request):
    return render(request, 'patient/dashboard_content.html')

def book_appointment(request):
    counties = County.objects.all()
    return render(request, 'patient/book_appointment.html',{'counties': counties})

@login_required(login_url='members/login_user/')
def view_doctor_by_county(request, county_id):
    county_doctor = Doctor.objects.filter(county=county_id).order_by('specialization')
    # user_session = request.user
    # user = User.objects.get(user=user_session)
    # check_pending = Appointment.objects.filter(user=user, status='Pending').count()
    # check_approved = Appointment.objects.filter(user=user, status='Approved').count()
    # check_appointments = check_pending + check_approved
    # 'check_appointments': check_appointments
    # detail = {
    #     'doctor_list': county_doctor, 
        
    #     }
    return render(request, 'patient/doctor_by_county.html', { 'county_doctor': county_doctor })


# DOctor side

def base_doctor(request):
    return render( request, 'doctor/base.html')

def doctor_dashboard(request):
    return render( request, 'doctor/dashboard.html')

def doctor_schedule(request, doctor_id):
    doctor_schedule = Doctor.objects.get(pk=doctor_id)
    return render(request, 'doctor/schedule.html', {'doctor_schedule': doctor_schedule})











def show_county(request, county_id):
    county = County.objects.get(pk=county_id)
    return render(request, 'county/show_county.html',{'county': county})



@login_required(login_url='/members/login_user/')
def counties(request):
    counties = County.objects.all()
    return render(request, 'county/counties.html', {'counties': counties})


def region(request):
    return render(request, 'doctor/region.html')



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
            user = User.objects.get(username=username)
            print(user.username)
            print(user.first_name)
            user_data = Patient.objects.create(user=user, phone=phone, gender=gender, birth_date=birth_date)
            user_data.save()

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration succesful"))
            return redirect('home')

    else:
        form = RegisterUserForm()
    return render(request,'home/register_patient.html', {'form': form} )


def register_user(request):
    if request.method == "POST":
        form = RegisterDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            birth_date = form.cleaned_data.get('birth_date')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = User.objects.get(username=username)
            print(user.username)
            print(user.first_name)
            user_data = Doctor.objects.create(user=user, phone=phone, gender=gender, birth_date=birth_date)
            user_data.save()

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration succesful"))
            return redirect('home')

    else:
        form = RegisterDoctorForm()
    return render(request,'home/register_patient.html', {'form': form} )
def home(request):
    return render(request, 'home/index.html')


@login_required(login_url='/register')
def doctor(request):
    return render(request, 'doctor/doctor.html')

