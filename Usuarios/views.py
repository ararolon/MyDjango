from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


def eliminar_usuario(request):
    """
    Vista para eliminar usuarios del sistema
    :param request: Httprequest object
    :return: HttpResponse
    """
    #se obtienen todos los usuarios del sistema
    usuarios= User.objects.all()
    contexto = {'usuarios':usuarios}
    return render(request,"Usuarios/eliminar.html",context=contexto)
