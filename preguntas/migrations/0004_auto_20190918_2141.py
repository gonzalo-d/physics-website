# Generated by Django 2.2.1 on 2019-09-18 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('preguntas', '0003_pregunta_usuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pregunta_usuario',
            new_name='ejercicio_usuario',
        ),
    ]
