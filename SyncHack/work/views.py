from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
from .models import Employee



def Signupview(request):
    all_employees = Employee.objects.all
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful')
            return render(request, 'work\dashboard.html', {'all': all_employees})
    else:
        form = SignUpForm()
        return render(request, 'work\Signup.html')

