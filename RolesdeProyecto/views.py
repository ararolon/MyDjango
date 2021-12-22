from django.shortcuts import render, redirect

# Create your views here.
import RolesdeProyecto
from RolesdeProyecto.forms import RolesProyectoForms
from RolesdeProyecto.models import RolesDeProyecto


def vista_principal(request):
    """
    vista principal de roles de proyecto
    :param request: HttpRequest object
    :return: HttpResponse
    """

    return render(request,"RolesdeProyecto/index_rol_proyecto.html")

def crear_nuevo_rol(request):
    """
    vista que permite crear un nuevo rol de proyecto en el sistema
    :param request: HttpRequest object
    :return: HttpResponse, HttpRedirect
    """
    formulario = RolesProyectoForms()

    if request.method == 'POST':
        formulario = RolesProyectoForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_rol_proyecto')

    return render(request, 'RolesdeProyecto/nuevo_rol.html', {'formulario': formulario})

def modificar_rol(request,pk):
    """
    Vista que permite la modificacion de un rol de proyecto en el sistema
    :param request: HttpRequest object
    :param pk: id del rol
    :return: HttpResponse
    """
    rol = RolesDeProyecto.objects.get(id=pk)
    form = RolesProyectoForms(instance=rol)

    if request.method == 'POST':
        form = RolesProyectoForms(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('index_rol_proyecto')

    context = {'formulario': form}
    return render(request, 'RolesdeProyecto/Modificar_rol.html', context)

def eliminar_rol(request,pk):
    """
    Vista para eliminar un rol de proyecto del sistema
    :param request: HttpRequest object
    :param pk: id del rol
    :return: HttpResponse, HttpRedirect
    """

    rol = RolesDeProyecto.objects.get(id=pk) #obtiene el objeto con el id

    if request.method == 'POST':

        try:
            rol.delete()
            #ideal usar messages
            return redirect('listar_roles')
        except Exception:
            #usar django messages framework
            print("No se puede eliminar, el rol esta en uso")
            return redirect('index_rol_proyecto')

    return render(request, 'RolesdeProyecto/eliminar_rol.html', {'rol':rol})


def listar_roles(request):
    """
    vista para listar todos los roles de proyecto en el sistema
    :param request: HttpResponse
    :return: HttpResponse
    """
    rol = RolesDeProyecto.objects.all()
    return render(request,"RolesdeProyecto/Listar_roles_proyecto.html",{'roles':rol})



def detalles_rol(request,pk):
    """
    Vista para ver todos los detalles de un rol
    :param request: HttpRequest object
    :param pk: id del rol
    :return: HttpResponse
    """
    rol = RolesDeProyecto.objects.get(id=pk)
    return render(request,"RolesdeProyecto/ver_detalles.html",{'rol':rol})

