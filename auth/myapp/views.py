from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('user_login')
    else:
        form = RegistrationForm()
    return render(request, 'myapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('hello_world')  # Redirect to 'hello_world' upon successful login
            else:
                messages.error(request, 'Invalid login credentials.')
        else:
            messages.error(request, 'Invalid form input. Please check the fields.')
    else:
        form = LoginForm()

    return render(request, 'myapp/login.html', {'form': form})


@login_required
def hello_world(request):
    return render(request, 'myapp/helloworld.html', {'user': request.user})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('user_login')
