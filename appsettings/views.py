from django.shortcuts import render

# Create your views here.


def settings_home(request):
    return render(request, 'settings/settings_home.html')
