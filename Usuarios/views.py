from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from SSO.decorador import vista_admin
from Usuarios.models import Usuario

@login_required(login_url='login')
@vista_admin
def index_usuarios(request):
    """
     Vista que muestra los usuarios del sistema
    :param request: Httprequest object
    :return: HttpResponse
    """
    usuarios = list(User.objects.filter(groups__name='usuarios'))
    return render(request, 'Usuarios/index_usuarios.html', {'usuarios': usuarios})


@login_required(login_url='login')
@vista_admin
def ver_detalles(request, id):
    """
    Vista que muestra mas detalles sobre un usuario en especifico seleccionado por id
    :param request: Httprequest object
    :param id: el id de un usuario
    :return: HttpResponse
    """
    # obtiene el usuario por medio del id
    usuario = get_object_or_404(User, pk=id)

    # si es que el usuario existe, se envia el objecto
    if usuario:
        return render(request, 'Usuarios/VerDetalles.html', {'usuario': usuario})

@login_required(login_url='login')
@vista_admin
def index_eliminarusuario(request):
    """
    Vista que muestra la lista de usuarios para eliminarlos del sistema
    :param request: Httprequest object
    :return: HttpResponse
    """
    # se obtienen todos los usuarios del sistema
    usuarios = list(User.objects.filter(groups__name='usuarios'))
    return render(request, "Usuarios/index_eliminar.html", {'usuarios': usuarios})

@login_required(login_url='login')
@vista_admin
def eliminar_usuario(request, id):
    """
     Vista que elimina un usuario del sistema
    :param request: HttpRequest object
    :param id: id del usuario a eliminar
    :return: HttpResponse o HttpRedirect
    """
    usuario = get_object_or_404(User, pk=id)
    if request.method == "POST":
        usuario.delete()
        return redirect('indexeliminar')
    else:
        return render(request, 'Usuarios/eliminar.html', {'usuario': usuario})
