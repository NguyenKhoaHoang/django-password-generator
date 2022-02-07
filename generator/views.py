from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOQPRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    admin = "Nguyễn Khoa Hoàng"
    function_page = "Random password"
    return render(request, 'generator/about.html', {'admin':admin, 'function_page':function_page})
