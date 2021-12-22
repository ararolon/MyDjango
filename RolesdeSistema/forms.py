from django import forms
from django.contrib.auth.models import Permission
from RolesdeSistema.models import RolesdeSistema


class RolesDeSistemaForms(forms.ModelForm):
    """
    Formulario para la creacion de roles de sistema
    clase padre: ModelForm
    """

    def __init__(self, *args, **kwargs):
        """
        clase padre : modelo RolesdeSistema
        subclase : formulario RolesDeSistemaForms

        Constructor de formulario, pasamos la clase formulario a la clase padre
        """
        super(RolesDeSistemaForms, self).__init__(*args, **kwargs)

        # Agregamos un campo personalizado para seleccionar los permisos del rol
        # widget de seleccion multiple
        # Se indica que los valores que pueden seleccionarse son los permisos filtrados con nombre "pp"
        self.fields['permisos'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                            choices=[(p.id, p.name) for p in Permission.objects.all() if
                                                                     p.codename.startswith("ps_")])
    class Meta:

        #Se indica el modelo que utiliza y los campos a utilizar
        model = RolesdeSistema
        fields = ['nombre','descripcion','permisos']

