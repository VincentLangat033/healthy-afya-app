from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register_user, name="register-patient"),
    path('doctor/', views.doctor, name="doctor"),
    path('doctor/region/', views.doctor_region, name= 'doctor-region'),
    path('doctor/region/<int:id>', views.region, name= 'specific-region'),
]