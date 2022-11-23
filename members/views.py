from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import  messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm



def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # phone = form.cleaned_data.get('phone')
            # gender = form.cleaned_data.get('gender')
            # birth_date = form.cleaned_data.get('birth_date')
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            # user = User.objects.get(username=username, password=password)
            # user_data = Patient.objects.create(user=user, phone=phone, gender=gender, birth_date=birth_date, first_name=first_name, last_name=last_name)
            # user_data.save()

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration succesful"))
            if user.is_super_user:
                return redirect('patient/dashboard')
            else:
                return redirect('home')

            

    else:
        form = RegisterUserForm()
    return render(request,'authenticate/register_user.html', {'form': form} )





# def register_user(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, ("Registration succesful"))
#             return redirect('home')

#     else:
#         form = UserCreationForm()
#     return render(request,'authenticate/register_user.html', {'form': form} )


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('home')
            # elif :
            #     return redirect('/doctor/dashboard') 
            else:
                return redirect('/patient/dashboard/content')

               
            # Redirect to a success page.
            ...
        else:
            messages.success(request, ('There was an eror logging in, Please try again..'))
            return redirect('login')

            # Return an 'invalid login' error message.
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('Log out Successful'))
    return redirect('home')



