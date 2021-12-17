
from django import forms
from django.contrib.auth.models import Permission

from RolesdeProyecto.models import RolesDeProyecto


class RolesProyectoForms(forms.ModelForm):

    """
    Formulario utilizado para la creacion y modificacion de los roles de Proyectos

    clase padre: forms.Form
    """

    def __init__(self,*args,**kwargs):

        """
        clase padre : modelo RolesdeProyecto
        subclase : formulario RolesdeProyectoForms

        Constructor de formulario, pasamos la clase formulario a la clase padre
        """
        super(RolesProyectoForms,self).__init__(*args,**kwargs)

        #Agregamos un campo personalizado para seleccionar los permisos del rol
        #widget de seleccion multiple
        #Se indica que los valores que pueden seleccionarse son los permisos filtrados con nombre "pp"
        self.fields['permisos']= forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple ,
                                                           choices=[(p.id, p.name) for p in Permission.objects.all() if
                                                                     p.codename.startswith("pp_")])



    class Meta:

        #Se indica el modelo que utiliza y los campos a utilizar
        model = RolesDeProyecto
        fields = ['nombre','descripcion','permisos']