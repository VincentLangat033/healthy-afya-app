from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import  messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import Patient, County, Doctor, Appointment, Schedule
from .utility import appointment_availability
from .decorators import unauthenticated_user, allowed_users, home_redirect


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
    user_email = request.user.email
    form = BookAppointmentForm(request.POST)
    if form.is_valid():
        appointment_date = form.cleaned_data.get('appointment_date')
        symptoms = form.cleaned_data.get('symptoms')
        appointment_data = Appointment.objects.create(appointment_date=appointment_date, symptoms=symptoms, user=user, doctor=doctor)
        appointment_data.save()
        email = EmailMessage(
            'Your Appointment Update',
            f'Greetings {user},\nThank you for booking an appointment with {doctor} on {appointment_date} Your Appointment is pending, you will get an email again once your doctor approves',
            settings.EMAIL_HOST_USER,
            [user_email]
        )   
        email.fail_silently = True
        email.send()
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

@login_required(login_url='members/login_user/')
@allowed_users(allowed_roles=['doctors'])
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


@login_required(login_url='/members/login_user/')
def view_all_appointments(request):
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
    return render(request, 'patient/view_all_appointments.html', context=context)

@login_required(login_url='/members/login_user/')
def patients_appointments(request):
    user = request.user
    doctor = Doctor.objects.get(user=user)
    pending_appointments = Appointment.objects.filter(doctor=doctor, status='Pending')
    approved_appointments = Appointment.objects.filter(doctor=doctor, status='Approved')
    rejected_appointments = Appointment.objects.filter(doctor=doctor, status='Rejected')
    context = {
        'pending_appointments': pending_appointments,
        'approved_appointments': approved_appointments,
        'rejected_appointments': rejected_appointments,
        'doctor' : doctor,
    }
    return render(request, 'doctor/appointments.html', context=context)


def patient_reviews(request):
    return render(request, 'patient/review.html')

def all_doctors(request):
    doctor = Doctor.objects.all()
    return render(request, 'patient/doctors.html', {'doctor': doctor})

def view_appointment(request, appointment_id):
    appointment_data = Appointment.objects.get(id=appointment_id)
    context = {'appointment_data': appointment_data}
    return render(request, 'doctor/view_appointment.html', context=context)

def approve_appointment(request, appointment_id):
    appointment_data = Appointment.objects.get(id=appointment_id)
    doctor_data = {}
    doctor_first_name = appointment_data.doctor.user.first_name
    doctor_last_name = appointment_data.doctor.user.last_name
    doctor_specialization = appointment_data.doctor.specialization
    symptoms = appointment_data.symptoms
    doctor_data['first_name'] = doctor_first_name
    doctor_data['last_name'] = doctor_last_name
    doctor_data['specialization'] = doctor_specialization
    form = ApproveAppointmentForm(request.POST or None, instance=appointment_data)
    if form.is_valid():
        date = form.cleaned_data.get('appointment_date')
        # user_email = request.patient.email
        # form.save()
        # email = EmailMessage(
        #     'Your Appointment Update',
        #     f'Greetings {user},\nThank you for booking an appointment with {doctor} on {date} Your Appointment is pending, you will get an email again once your doctor approves',
        #     settings.EMAIL_HOST_USER,
        #     [user_email]
        # )   
        # email.fail_silently = True
        # email.send()
        return redirect('doctor-dashboard')
    schedule_data = {}
    user = request.user
    doctor = Doctor.objects.get(user=user)
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
    return render(request, 'doctor/approve_appointment.html', context=context)


def reject_appointment(request, appointment_id):
    appointment_data = Appointment.objects.get(id=appointment_id)
    form = RejectAppointmentForm(request.POST or None, instance=appointment_data)
    if form.is_valid():
        form.save()
        return redirect('doctor-dashboard')
    context = {'form': form}
    return render(request, 'doctor/reject_appointment.html', context=context)














def show_county(request, county_id):
    county = County.objects.get(pk=county_id)
    return render(request, 'county/show_county.html',{'county': county})



@login_required(login_url='/members/login_user/')
def counties(request):
    counties = County.objects.all()
    return render(request, 'county/counties.html', {'counties': counties})


def region(request):
    return render(request, 'doctor/region.html')


@unauthenticated_user
@home_redirect
def registration_dashboard(request):
    return render(request,'home/registration_dashboard.html')


@home_redirect
def registere_doctor(request):
    userForm = DoctorUserForm()
    doctorForm = DoctorForm()

    if request.method == 'POST':
        userForm = DoctorUserForm(request.POST)
        doctorForm = DoctorForm(request.POST)
        if userForm.is_valid() and doctorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            doctor = doctorForm.save()
            doctor.user = user
            doctor = doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='doctors')
            my_doctor_group[0].user_set.add(user)
        return redirect('login')
    context = {'userForm': userForm, 'doctorForm': doctorForm}


    return render(request, 'home/register_doctor.html', context)
    

@unauthenticated_user
@home_redirect
def register_patient(request):
        form = RegisterUserForm()
        
        mydict={'form':form}
        if request.method == "POST":
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                # user = form.save()
                # group = Group.objects.get(name='patient')
                # user.groups.add(group)
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
                group = Group.objects.get(name='patient')
                user.groups.add(group)
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, ("Registration succesful"))
                return redirect('home')
        else:
            # return render(request,'home/register_patient.html',context=mydict )            
            return render(request,'home/register_patient.html', {'form': form} )

@unauthenticated_user
def register_user(request):
    if request.method == "POST":
        form = RegisterDoctorForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='doctors')
            user.groups.add(group)
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



@login_required(login_url='/members/login_user/')
def register_doctor(request):
    user_data = request.user
    if request.method == 'POST':
        form = DoctorApplicationForm(request.POST)
        if form.is_valid():
            specialization = form.cleaned_data.get('specialization')
            county = form.cleaned_data.get('county')
            biography = form.cleaned_data.get('biography')
            application_data = RegisterDoctor.objects.create(user=user_data, specialization=specialization, county=county, biography=biography)
            application_data.save()
            return redirect('/patient/dashboard/content')
    else:
        form = DoctorApplicationForm()
    return render(request, 'patient/doctor_application.html', {'form': form})


def schedule(request):
    if Doctor.objects.filter(user = request.user).exists():
        dock = Doctor.objects.get(user = request.user)
    else:
        return HttpResponse("No such Doctor Found")
    form = DoctorScheduleForm()
    if request.method == 'POST':
        form = DoctorScheduleForm(request.POST)
        if form.is_valid():
            if Schedule.objects.filter(doctor =dock).exists():
               Schedule.objects.get(doctor=dock).delete()
               print("Overwriting the doctor object") 
            monday = form.cleaned_data.get('monday')
            tuesday = form.cleaned_data.get('tuesday')
            wednesday = form.cleaned_data.get('wednesday')
            thursday = form.cleaned_data.get('thursday')
            friday = form.cleaned_data.get('friday')
            schedule = Schedule(monday=monday,tuesday=tuesday,thursday=thursday,wednesday=wednesday,friday=friday, doctor=dock)
            schedule.save()
            messages.success(request, "Success: Schedule created.")
        return redirect('doctor-dashboard')

    return render(request, 'doctor/schedule.html',{'form':form})
