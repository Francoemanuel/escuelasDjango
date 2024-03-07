from io import BytesIO
from pydoc import describe
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Escuela
from . forms import EscuelaForm
from persona.models import Alumno
from django.core.files.storage import FileSystemStorage

import pandas as pd
from django.contrib import messages
from xlrd import XLRDError

# Create your views here.
def index(request):
    print(request)
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
    

def reportes(request):
    if  request.method == "GET":
        return render(request, "escuela/reportes.html")
    
    if request.method == "POST" and request.FILES.get("archivo"):
        mi_archivo_excel = request.FILES["archivo"]
        
        # Procesar el archivo Excel
        df = pd.read_excel(mi_archivo_excel)
        # print(df)


        nuevo_df = pd.DataFrame({
        'estado': 'vigente',
        'documento': df['documento'],
        'fecha_desde': df['fecha_desde'],
        'fecha_hasta': df['fecha_hasta'],
        'nro_expediente': df['nro_expendiente'],
        })
        
        nuevo_df.to_excel("recupero_de_haberes_notificacion.xlsx", index=False)

        print(nuevo_df)
        print("Nuevo archivo Excel guardado exitosamente.")
        
        # Hacer algo con el DataFrame, por ejemplo, mostrarlo en una respuesta HTTP
        html = df.to_html()
        return HttpResponse(html)