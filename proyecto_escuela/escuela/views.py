from io import BytesIO
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Escuela
from . forms import EscuelaForm
from persona.models import Alumno

import pandas as pd

# Create your views here.
def index(request):
    escuela = Escuela.objects.all()
    context = {
        'escuelas': escuela,
        # 'dataframe': df,
    }
    return render(request, 'escuela/index.html', context)

def excel(request):
    # Obtener todos los datos de las escuelas desde la base de datos
    escuelas = Escuela.objects.all()

    # Crear un DataFrame de Pandas con los datos de las escuelas
    data = {
        'Nombre': [escuela.nombre for escuela in escuelas],
        'Número': [escuela.numero for escuela in escuelas],
        'Departamento': [escuela.departamento for escuela in escuelas]
    }
    df = pd.DataFrame(data)

    # Crear un objeto BytesIO para escribir el archivo Excel
    excel_data = BytesIO()

    # Crear un escritor de Excel con XlsxWriter
    with pd.ExcelWriter(excel_data, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)

    # Establecer la posición del cursor al principio del objeto BytesIO
    excel_data.seek(0)

    # Devolver el archivo Excel como respuesta HTTP para su descarga
    response = HttpResponse(excel_data.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="escuelas.xlsx"'
    return response

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
    