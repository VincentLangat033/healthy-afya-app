from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register_patient, name="register-patient"),
    path('register_doctor/', views.registere_doctor, name= 'register-doctor'),
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
    path('patient/doctor_application', views.register_doctor, name= 'doctor-application'), 
    path('registration_dashboard', views.registration_dashboard, name= 'registration-dashboard'), 
    

    # Doctor routes base_doctor
    path('doctor/', views.base_doctor, name= 'base-doctor'),
    path('doctor/dashboard', views.doctor_dashboard, name= 'doctor-dashboard'),
    path('doctor/dashboard/doctor-schedule/', views.doctor_schedule, name= 'doctor-schedule'),
    path('view_appointments/', views.view_appointments, name='view-appointments'),
    path('patients_appointments/', views.patients_appointments, name='patient-appointments'),
    path('approve/<appointment_id>', views.approve_appointment, name='approve'),
    path('reject/<appointment_id>',views.reject_appointment, name='reject'),
    path('appointment_details/<appointment_id>',views.view_appointment, name='appointment-details'),
    path('doctor/schedule',views.schedule, name='schedule'),

    # Forgot password URLS
    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name = "passwords/password_reset.html"), 
    name = 'reset_password'),
    
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset_password_complete/', 
    
    auth_views.PasswordResetCompleteView.as_view(template_name = "passwords/password_reset_complete.html"), 
    name='password_reset_complete'),



]


    # path('doctor/', views.doctor, name="doctor"),
    # path('doctor/region/', views.doctor_region, name= 'doctor-region'),
    # path('patient/dashboard', views.region, name= 'specific-region'),

#  - Submit email form   // PasswordResetView.as_view()
#  - Email sent success message  // PasswordResetDoneView.as_view()
#  -Link to password Reset from in email   // PasswordResetConfirmView.as_view()
#  - Password successfully changed message   // PasswordResetCompleteView.as_view()
    