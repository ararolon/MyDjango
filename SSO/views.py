from django.http import request
from django.shortcuts import render, redirect

# Create your views here.

"""
Vista para login al sistema
"""
def login(request):
    return redirect('/accounts/google/login/?process=login')

"""
Vista que permite el logout del sistema
"""

def logout(request):
    return redirect('/accounts/logout/')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'SSO/Home.html', context=None)
    else:
       return redirect('login')