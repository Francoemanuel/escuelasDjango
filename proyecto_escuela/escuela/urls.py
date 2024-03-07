from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'escuela'),
    path('view/<int:id>', views.view, name='escuela_view'),
    path('edit/<int:id>', views.edit, name='escuela_edit'),
    path('new/', views.new, name='escuela_new'),
    path('excel/', views.excel, name='escuela_excel'),
    path('reportes/', views.reportes, name='reportes'),
]
