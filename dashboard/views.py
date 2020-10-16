from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def signupuser(request):
    # Create user in built in authentication module
    if request.method == 'GET':
        return render(request, 'dashboard/signupuser.html', {'form': UserCreationForm()})
    else:
        # Create a new device if POST type
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Take variables from post and create new user object with them.
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                # Save the object into the database.
                user.save()
                # Login the user
                login(request, user)
                # Return the user to the dashboard
                return redirect('dashboard:dashboard')
            # If IntegrityError exist, display error on signup page
            except IntegrityError:
                return render(
                    request, 'dashboard/signupuser.html',
                    {'form': UserCreationForm(),
                     'error': 'That username is already taken. Try again.'}
                )
        else:
            # If passwords don't match, display error on signup page
            return render(
                request, 'dashboard/signupuser.html',
                {'form': UserCreationForm(),
                 'error': 'Passwords did not match.  Try again.'}
            )


def dashboard(request):
    return render(request, "dashboard/dashboard.html")


def uialerts(request):
    return render(request, "dashboard/ui-alerts.html")


def uialerts(request):
    return render(request, "dashboard/ui-alerts.html")


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('dashboard:dashboard')


def loginuser(request):
    # Create user in built in authentication module
    if request.method == 'GET':
        return render(request, 'dashboard/login.html')
    else:
        user = authenticate(request, username=request.POST['username1'], password=request.POST['password1'])
        if user is None:
            return render(request, 'dashboard/login.html', {'error': 'Username and password do not match.'})
        else:

            # Login the user
            login(request, user)
            return redirect('dashboard:dashboard')

