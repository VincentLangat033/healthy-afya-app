from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register_patient, name="register-patient"),
    path( 'counties/', views.counties, name='counties'),
    path( 'show-county/<county_id>/', views.show_county, name='county'),
    path('patient/dashboard/', views.patient_dashboard, name= 'patient-dashboard'),
    path('patient/dashboard/content', views.dashboard_content, name= 'dashboard-content'),
    path('patient/dashboard/content/book-appointment', views.book_appointment, name= 'book-appointment'),
    path('patient/dashboard/content/doctor-by-county/<county_id>', views.view_doctor_by_county, name= 'doctor-by-county'),
    path('patient/dashboard/appointment-form/<doctor_id>', views.appointment_form, name= 'appointment-form'),
    path('view_all_appointments/', views.view_all_appointments, name='view-_all-appointments'),
    path('patient_reviews/', views.patient_reviews, name='patient-reviews'),
    path('all_doctors/', views.all_doctors, name='all-doctors'),

    # Doctor routes base_doctor
    path('doctor/', views.base_doctor, name= 'base-doctor'),
    path('doctor/dashboard', views.doctor_dashboard, name= 'doctor-dashboard'),
    path('doctor/dashboard/doctor-schedule/', views.doctor_schedule, name= 'doctor-schedule'),
    path('view_appointments/', views.view_appointments, name='view-appointments'),
    path('patients_appointments/', views.patients_appointments, name='patient-appointments'),
    path('approve/<appointment_id>', views.approve_appointment, name='approve'),
    path('reject/<appointment_id>',views.reject_appointment, name='reject'),


]


    # path('doctor/', views.doctor, name="doctor"),
    # path('doctor/region/', views.doctor_region, name= 'doctor-region'),
    # path('patient/dashboard', views.region, name= 'specific-region'),
    