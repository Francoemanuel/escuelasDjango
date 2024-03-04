from django.shortcuts import render
from django.views import generic
from io import BytesIO
from django.db import connections
from django.http import HttpResponse


from .models import Persona, Alumno
from helpers.sql import dictfetchall

import pandas as pd


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

def reportes(request):
    print('hola')
    if request.method == "GET":
        with connections["default"].cursor() as cursor:
            cursor.execute(
                """SELECT  a.nombre_padre, a.apellido_padre 
                FROM persona_alumno as a""",
            )

            result = dictfetchall(cursor)
            print(result)


# def excel(request):
#     alumnos = Alumno.objects.all()

#     # Crear un DataFrame de Pandas con los datos de las escuelas
#     data = {
#         'Nombre padre': [alumno.nombre_padre for alumno in alumnos],
#         'Apellido padre': [alumno.apellido_padre for alumno in alumnos],
#         'Nombre madre': [alumno.nombre_madre for alumno in alumnos],
#         'Apellido madre': [alumno.nombre_madre for alumno in alumnos],
#         'nro_contacto': [alumno.nombre_madre for alumno in alumnos]
#     }
#     df = pd.DataFrame(data)

#     # Crear un objeto BytesIO para escribir el archivo Excel
#     excel_data = BytesIO()

#     # Crear un escritor de Excel con XlsxWriter
#     with pd.ExcelWriter(excel_data, engine='xlsxwriter') as writer:
#         df.to_excel(writer, index=False)

#     # Establecer la posición del cursor al principio del objeto BytesIO
#     excel_data.seek(0)

#     # Devolver el archivo Excel como respuesta HTTP para su descarga
#     response = HttpResponse(excel_data.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = 'attachment; filename="escuelas.xlsx"'
#     return response    