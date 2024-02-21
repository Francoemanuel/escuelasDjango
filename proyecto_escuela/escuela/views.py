from django.shortcuts import render
from .models import Escuela

# Create your views here.
def index(request):
    escuela = Escuela.objects.all()
    context = {
        'escuelas': escuela
    }
    return render(request, 'escuela/index.html', context)