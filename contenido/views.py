from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
from contenido.models import materia
from preguntas.models import ejercicio, ejercicio_usuario
from .forms import TopicoForm
import os

context = dict()


@login_required(login_url='login')
def material(request):
  if request.method == 'POST':
    if "materia" in request.POST.keys():
      consulta = request.POST.getlist('materia')
      context["submaterias"] = materia.objects.filter(topico__in=consulta).values("subtopico").order_by().distinct()
      context["materia"] = consulta
      return render(request, 'eleccion-submaterial.html', context)

    elif "submateria" in request.POST.keys():
      consulta = request.POST.getlist('submateria')
      materias = materia.objects.filter(topico__in=context["materia"], subtopico__in=consulta).order_by().distinct()
      id_materia = []
      for i in materias:
        id_materia.append(i)
      context["preguntas"] = ejercicio.objects.filter(materia__in=id_materia).values("ruta",
                                                                                     "materia__subtopico").order_by()
      context["submateria"] = consulta
      return render(request, 'mostrar-material.html', context)

  context["materias"] = materia.objects.values("topico").order_by().distinct()
  return render(request, 'eleccion-material.html', context)


@login_required(login_url='login')
def libro_pdf(request):
  if request.method == 'POST':
    if "pdf_ruta" in request.POST.keys():
      pdf = open(request.POST["pdf_ruta"], 'rb')
      pdf.seek(0)
      return FileResponse(pdf, as_attachment=False, filename='fisica.pdf')
