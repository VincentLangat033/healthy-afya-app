from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import  messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, RegisterDoctorForm, BookAppointmentForm
from .models import Patient, County, Doctor, Appointment, Schedule
from .utility import appointment_availability


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
    # print(county_doctor)
    return render(request, 'patient/doctor_by_county.html', { 'county_doctor': county_doctor })

def appointment_form(request, doctor_id):
    schedule_data = {}
    pk = doctor_id
    user_data = request.user
    current_user = user_data.id
    print(user_data)
    # user = User.objects.get(id=user_data)
    user = User.objects.get(pk=request.user.pk)
    doctor = Doctor.objects.get(id=pk)
    form = BookAppointmentForm(request.POST)
    if form.is_valid():
        appointment_date = form.cleaned_data.get('appointment_date')
        symptoms = form.cleaned_data.get('symptoms')
        appointment_data = Appointment.objects.create(appointment_date=appointment_date, symptoms=symptoms, user=user, doctor=doctor)
        appointment_data.save()
        return render(request, 'patient/dashboard.html')
    else:
        form = BookAppointmentForm()
    doctor_schedule = Schedule.objects.get(doctor=doctor)
    schedule_data['monday'] = doctor_schedule.monday
    schedule_data['tuesday'] = doctor_schedule.tuesday
    schedule_data['wednesday'] = doctor_schedule.wednesday
    schedule_data['thursday'] = doctor_schedule.thursday
    schedule_data['friday'] = doctor_schedule.friday
    schedule_data['saturday'] = doctor_schedule.saturday
    schedule_data['sunday'] = doctor_schedule.sunday
    filtered_schedule = appointment_availability(schedule_data)
    context = {'form': form, 'filtered_schedule': filtered_schedule}
    return render(request, 'patient/appointment_form.html', context=context)


# DOctor side

def base_doctor(request):
    return render( request, 'doctor/base.html')

def doctor_dashboard(request):
    return render( request, 'doctor/dashboard.html')

def doctor_schedule(request):
    # doctor_schedule = Doctor.objects.get(pk=doctor_id)
    current_user = request.user
    user=current_user
    print(user)
    # doctor_schedule = Doctor.objects.get()
    doctor = Doctor.objects.get(user=user)
    schedule = Schedule.objects.get(doctor=doctor)
    print(doctor_schedule)
    return render(request, 'doctor/schedule.html', {'doctor': doctor, 'schedule': schedule})

@login_required(login_url='/members/login_user/')
def view_appointments(request):
    # user_session = request.user
    user_status = User.objects.get(pk =request.user.pk)
    pending_appointments = Appointment.objects.filter(user=user_status , status='Pending')
    approved_appointments = Appointment.objects.filter(user=user_status , status='Approved')
    rejected_appointments = Appointment.objects.filter(user=user_status , status='Rejected')
    context = {
        'pending_appointments': pending_appointments,
        'approved_appointments': approved_appointments,
        'rejected_appointments': rejected_appointments,
        }
    return render(request, 'doctor/appointments.html', context=context)











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

