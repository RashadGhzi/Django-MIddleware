from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    print('We are in view function.')
    return HttpResponse('This is home with view')
