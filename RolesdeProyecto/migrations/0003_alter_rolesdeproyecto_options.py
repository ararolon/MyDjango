# Generated by Django 3.2.7 on 2021-12-21 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RolesdeProyecto', '0002_auto_20211221_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rolesdeproyecto',
            options={'permissions': [('pp_proyecto', 'Administrar roles de proyecto'), ('pp_rol', 'Administrar roles de proyecto'), ('pp_sprint', 'Administrar sprint'), ('pp_us', 'Administrar Us'), ('pp_product_backlog', 'ver product backlog'), ('pp_sb', 'administrar sprint backlog'), ('pp_kanban', 'Administrar kanban'), ('pp_us_QA', 'desplazar user story a QA'), ('pp_bc', 'cargar horas de trabajo')]},
        ),
    ]
