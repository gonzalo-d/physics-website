# Generated by Django 2.2.1 on 2019-10-06 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0005_auto_20191006_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudio',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenido.materia'),
        ),
    ]
