from django.shortcuts import render

# Create your views here.


def provisioning_home(request):
    return render(request, 'provisioning/provisioning_home.html')

