from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    print('We are in view function.')
    a = 10/0
    return HttpResponse('This is home with view')
