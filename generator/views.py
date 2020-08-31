from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    my_password = ''
    length = int(request.GET.get('passLength', 12))

    # request.GET.get - gets the varibles we enterd in the html files
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    for i in range(length):
        my_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': my_password})


def about(request):
    return render(request, 'generator/about.html')
