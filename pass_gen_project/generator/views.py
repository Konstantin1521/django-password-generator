from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html.')


def secret(request):
    return HttpResponse('<h1>you are curious,i like you</h1>')


def password(request):
    
    Characters = list('abcdefghijklmnopqrstuvwxyz')

    lenght = int(request.GET.get('length', 12))

    thepassword = ''

    if request.GET.get('uppercase'):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        Characters.extend(list('!@#$%^&*()_+-=?.,":;}[]'))

    if request.GET.get('numbers'):
        Characters.extend(list('1234567890'))


    if lenght < 6:
        return HttpResponse('<h1>Недопустимое значения длины пароля</h1>')
    elif lenght > 14:
        return HttpResponse ('<h1>Недопустимое значения длины пароля</h1>')
    else:
        for x in range(lenght):
            thepassword += random.choice(Characters)

        return render(request, 'generator/password.html.', {'password':thepassword})
    

def about_me(request):
    return render(request, 'generator/index.html')

# Create your views here.
