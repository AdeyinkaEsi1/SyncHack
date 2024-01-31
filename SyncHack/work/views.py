from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, AddUserForm
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required



def WelcomeView(request):

    return render(request, 'home.html')


def RegisterView(request):
    user = None

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
             user_manager = UserProfile.objects
             user = user_manager.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                role=form.cleaned_data['role'],
            )
             if user:
                # send_signup_email(user)
                return redirect('login')

    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


# Adding users/staff - done by admin
@login_required(login_url='/login/')
def AddUserView(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # send_signup_email(user)

            return redirect('add_user')  
    else:
        form = AddUserForm()

    return render(request, 'add_user.html', {'form': form})



# Login Functionality
def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Check the user's role and redirect accordingly
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'employee':
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def LogoutView(request):
    logout(request)
    return redirect('home')

def DashboardView(request):
    
    return render(request, 'dashboard.html')

def AdminDashboardView(request):
    
    return render(request, 'admin_dashboard.html')