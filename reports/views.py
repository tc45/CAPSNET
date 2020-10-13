from django.shortcuts import render

# Create your views here.


def reports_home(request):
    return render(request, 'reports/reports_home.html')

