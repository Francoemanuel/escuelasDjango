from io import BytesIO
from django.shortcuts import render
from . models import Supervision
from django.http import HttpResponse

from django.db import connections

import pandas as pd
# Create your views here.

def index(request):
    supervision = Supervision.objects.all()
    context = {
        'supervisiones': supervision
    }
    return render(request, 'supervision/index.html', context)

def excel(request, id):
    supervision_id = id
    print(supervision_id)
    if request.method == "GET":
        with connections["default"].cursor() as cursor:
            cursor.execute(
                """SELECT s.nombre, e.numero, e.nombre
                FROM supervision_supervision s
                JOIN escuela_escuela e ON e.supervision_id =  s.id
                WHERE s.id = %s""",
                [supervision_id],
            )
            rows = cursor.fetchall()
           # Crear un DataFrame de Pandas con los resultados de la consulta
        df = pd.DataFrame(rows, columns=['Nombre Supervisión', 'Número Escuela', 'Nombre Escuela'])

        excel_data = BytesIO()

        with pd.ExcelWriter(excel_data, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)

        # Cerrar el objeto ExcelWriter para finalizar el archivo
        excel_data.seek(0)
    
        response = HttpResponse(excel_data.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="escuelas.xlsx"'
        return response

