from django.db import models


class Materia(models.Model):
  topico = models.CharField(blank=False, null=False, max_length=255)
  subtopico = models.CharField(blank=False, null=False, max_length=255)
