from django.db import models
from django.contrib.auth.models import Permission


# Create your models here.
class RolesdeSistema(models.Model):
    """
    Modelo para roles del sistema
    obs: Los roles del sistema no pueden ser eliminados

    clase padre : models.Model

    Atributo:
    nombre = nombre del rol
    descripcion =  descripcion breve del rol del sistema
    permisos = conjunto de permisos para el rol
    """
    nombre = models.CharField(max_length=20, blank=False, unique=True)
    descripcion = models.TextField(max_length=60, blank=True)
    permisos = models.ManyToManyField(Permission, blank=True)  # Indica que varios roles pueden tener varios permisos

    class Meta:
        """
        Pemisos asociados al administrador del sistema.
        """
        permissions = [
            # Usuarios = permisos para eliminar usuarios del sistema y habilitar usuarios en el sistema
            ("ps_usuarios", "Administrar usuarios en el sitema"),
            # Proyectos =  Crear proyectos en el sistema, insertar usuarios a un proyecto
            ("ps_proyectos", "Administrar proyectos e integrantes"),
            # Roles = Crear nuevos roles en el sistema, listar todos los roles de proyectos en el sistema
            ("ps_roles", "Administrar creacion de role en el sistema"),
        ]


    def __str__(self):
        return self.nombre


    def get_permisos(self):
        """
        Método que retorna los permisos asignados al rol.

        :return: lista de permisos
        """
        return [p for p in self.permisos.all()]