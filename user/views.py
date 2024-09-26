from django.shortcuts import render,redirect
from . forms import UserRegisterForm

#import authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f'Account created for {first_name,last_name}!login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=email ,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are now logged in as {email}')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')
