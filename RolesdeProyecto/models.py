from django.db import models
from django.contrib.auth.models import Permission


# Create your models here.
class RolesDeProyecto(models.Model):
    """
    Modelo para roles de proyecto

    clase padre : models.Model

    Atributo:
    nombre = nombre del rol
    descripcion =  descripcion breve del rol de proyecto
    permisos = conjunto de permisos para el rol
    """
    nombre = models.CharField(max_length=20, blank=False, unique=True)
    descripcion = models.TextField(max_length=60, blank=True)
    permisos = models.ManyToManyField(Permission, blank=True)  # Indica que varios roles pueden tener varios permisos

    class Meta:
        """
        Permisos disponible para rol de proyecto
        Algunos roles tienen  agrupados varios permisos como el de crear, eliminar, modificar.
        """
        permissions = [
            #Proyecto = configurar, inicial, finalizar o cancelar proyecto
            #Permiso habilitado para scrum master
            ("pp_proyecto","Administrar roles de proyecto"),

            #Roles= Crear, modificar, eliminar e importar roles
            #el rol se modifica a nivel de proyecto, asi para que no se modifique el rol creado por el administrador
            #el rol modificado es una copia
            #permiso habilitado para scrum master
            ("pp_rol","Administrar roles de proyecto"),

            #Sprint= permisos para configurar parametros inicales para el sprint, asignar horas, iniciar, finalizar,cancelar
            #asignar miembros al team developer del sprint.
            #Permiso habilitado para el scrum master
            #una vez iniciado el sprint,ya no puede modificarse
            ("pp_sprint","Administrar sprint"),

            #User story= permisos para crear, modificar, eliminar un user story, agregar una estimacion, asignar us a un usuario
            #ver detalles de us,asignar un estado final (released/cancelado)
            #permiso para el scrum master
            ("pp_us","Administrar Us"),

            #Produc backlog = ver los user stories
            ("pp_product_backlog","ver product backlog"),

            #Sprint Backlog = Ver user stories asignados a un usuario
            #permiso para miembros del team developer de un sprint.
            ("pp_sb","administrar sprint backlog"),

            #Kanban = Desplazar el us por el tablero (to-do/doing/done)
            ("pp_kanban","Administrar kanban"),
            # Para poner el user story en QA (Scrum master)
            ("pp_us_QA","desplazar user story a QA"),

            #Burndown chart = Cargar horas de trabajo
            ("pp_bc","cargar horas de trabajo"),
        ]


    def __str__(self):
        return self.nombre


    def get_permisos(self):
        """
        Método que retorna los permisos asignados al rol.

        :return: lista de permisos
        """
        return [p for p in self.permisos.all()]
