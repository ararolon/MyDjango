from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

# Create your views here.
from RolesdeSistema.forms import RolesDeSistemaForms
from RolesdeSistema.models import RolesdeSistema
from SSO.decorador import vista_admin


@login_required(login_url='login')
@vista_admin
def vista_principal(request):
    """
    vista principal de roles de sistema
    :param request: HttpRequest object
    :return: HttpResponse
    """

    return render(request,"RolesdeSistema/index_rol_sistema.html")

@login_required(login_url='login')
@vista_admin
def crear_nuevo_rol(request):
    """
    vista que permite crear un nuevo rol de proyecto en el sistema
    :param request: HttpRequest object
    :return: HttpResponse, HttpRedirect
    """
    formulario = RolesDeSistemaForms()

    if request.method == 'POST':
        formulario = RolesDeSistemaForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_rol_sistema')

    return render(request, 'RolesdeSistema/nuevo_rol.html', {'formulario': formulario})


@login_required(login_url='login')
@vista_admin
def modificar_rol(request,pk):
    """
    Vista que permite la modificacion de un rol de proyecto en el sistema
    :param request: HttpRequest object
    :param pk: id del rol
    :return: HttpResponse
    """
    rol = RolesdeSistema.objects.get(id=pk)
    form = RolesDeSistemaForms(instance=rol)

    if request.method == 'POST':
        form = RolesdeSistema(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('index_rol_sistema')

    context = {'formulario': form}
    return render(request, 'RolesdeSistema/Modificar_rol.html', context)

@login_required(login_url='login')
@vista_admin
def listar_roles(request):
    """
    vista para listar todos los roles de proyecto en el sistema
    :param request: HttpResponse
    :return: HttpResponse
    """
    rol = RolesdeSistema.objects.all()
    return render(request,"RolesdeSistema/Listar_roles_sistema.html",{'roles':rol})


@login_required(login_url='login')
@vista_admin
def detalles_rol(request,pk):
    """
    Vista para ver todos los detalles de un rol
    :param request: HttpRequest object
    :param pk: id del rol
    :return: HttpResponse
    """
    rol = RolesdeSistema.objects.get(id=pk)
    return render(request,"RolesdeSistema/ver_detalles.html",{'rol':rol})


