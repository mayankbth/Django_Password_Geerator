from django.shortcuts import render
# from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': 'ahfkfa236kbsf'})


# def eggs(request):
#     return HttpResponse('<h1>eggs are so tasty</h1>')


def password(request):
    
    length = int(request.GET.get('length', 12)) # 12 is default value
    
    charecters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('spcial'):
        charecters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        charecters.extend(list('0123456789'))
        
    thepassword = ''
    
    for x in range(length):
        thepassword += random.choice(charecters)
        
    return render(request, 'generator/password.html', {'password': thepassword} )


def about(request):
    return render(request, 'generator/about.html')

