from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

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
                login(request, user)
                return render(request, 'dashboard/dashboard.html'
                    )
            except IntegrityError:
                return render(
                    request, 'dashboard/signupuser.html',
                    {'form': UserCreationForm(),
                     'error': 'That username is already taken.'}
                )
        else:
            # Tell user passwords don't match.
            return render(
                request, 'dashboard/signupuser.html',
                {'form': UserCreationForm(),
                 'error': 'Passwords did not match.  Try again.'}
            )





def dashboard(request):
    return render(request, "dashboard/dashboard.html")


def uialerts(request):
    return render(request, "dashboard/ui-alerts.html")
