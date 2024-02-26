from django.shortcuts import render, redirect
from . models import Escuela
from . forms import EscuelaForm
from persona.models import Alumno

# Create your views here.
def index(request):
    escuela = Escuela.objects.all()
    context = {
        'escuelas': escuela
    }
    return render(request, 'escuela/index.html', context)

def view(request, id):
    escuela = Escuela.objects.get(id=id)
    alumnos = Alumno.objects.filter(escuela=escuela)
    context = {
        'escuela': escuela,
        'alumnos': alumnos,
    }
    return render(request, 'escuela/detail.html', context)

def edit(request, id):
    escuela = Escuela.objects.get(id=id)
    context = {
        'escuelas': escuela
    }
    return render(request, 'escuela/edit.html', context)

def new(request):
    if request.method == 'GET':
        form = EscuelaForm()
        context = {
            'form': form
        }
        return render(request, 'escuela/new.html', context)
    
    if request.method == 'POST':
        form = EscuelaForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('escuela')
    