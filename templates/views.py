from django.shortcuts import render

# Create your views here.


def templates_home(request):
    return render(request, 'templates/templates_home.html')

