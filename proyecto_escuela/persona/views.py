from django.shortcuts import render
from django.views import generic

from .models import Persona, Alumno


# Create your views here.
def index(request):
    persona = Persona.objects.all()
    context = {
        'personas': persona
    }
    return render(request, 'persona/index.html', context)

class alumno(generic.ListView):
    template_name = "alumno/index.html"
    context_object_name = "alumnos_list"

    def get_queryset(self):
        return Alumno.objects.all()

    # alumno = Alumno.objects.all()
    # context = {
    #     'alumnos': alumno
    # }
    # return render(request, 'alumno/index.html', context)