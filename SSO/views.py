from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from SSO.decorador import agregar_usuarios


def login(request):
    """
    Vista que redirecciona al SSO de google
    :param request: HttpRequest object
    :return: HttpRedirect
    """
    return redirect('/accounts/google/login/?process=login')

"""
Vista que permite el logout del sistema
"""


def logout(request):
    """
    Redirecciona a la pagina de cerrar sesion de google
    :param request: HttpRequest object
    :return:HttpRedirect
    """
    return redirect('/accounts/logout/')

@login_required(login_url='login')
@agregar_usuarios
def home(request):
    """
    Vista principal cuando se conecta un usuario
    :param:
        request (HttpRequest Object): respuesta del request
    :return
        El HttpResponse de la Vista a mostrarse
    """

    #pregunta si el usuario es el administrador
    if request.user.groups.filter(name='administrador'):
        return render(request, 'SSO/Home.html', context=None)
    elif request.user.groups.filter(name='usuarios'):
        return render(request,'SSO/Home_usuario.html',context=None)
    else:
        return redirect('login')



def configurariones_iniciales(request):

   """
    Se realizan las configuraciones iniciales para la identificacion de usuarios.
    Se crea un grupo administrador y de usuarios si es que todavia no existe en
    el sistema.
   :param request: HttpREquest object
   :return: HttpRedirect
   """
   #pregunta por el grupo administrador
   if not Group.objects.filter(name='administrador').exists():
       grupo = Group.objects.create(name='administrador')
       grupo.save()

   #pregunta por el grupo usuarios

   if not Group.objects.filter(name='usuarios'):
       grupo = Group.objects.create(name='usuarios')
       grupo.save()

   return redirect('home')




