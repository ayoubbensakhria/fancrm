from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
import datetime

from .forms import CustomUserCreationForm, CustomUserAuthForm, CustomUserChangeForm, CustomPasswordChangeForm, CustomPasswordResetForm

# Create your views here.
@login_required
def dashboard(request):
    time_delta = request.user.date_joined + datetime.timedelta (hours=request.user.duration)
    return render(request, 'dashboard.html', {'time_delta': time_delta})

def register(request):
    context = {}
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,user)
            return render(request,'dashboard.html')
    context['form']=form
    return render(request,'registration/register.html', context)

def signin(request):
    if request.method == 'POST':
        username = request.POST['username'] # <-- check forms to identify POST keys
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, 'You are Logged in !')
            return redirect('dashboard')                       
        else:
            messages.error(request, 'Wrong credentials', extra_tags='red')
            return redirect('login')
    else:

        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            form = CustomUserAuthForm()
            context = {'form': form}
            return render(request, 'registration/login.html', context)   