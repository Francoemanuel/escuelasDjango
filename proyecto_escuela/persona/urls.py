from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='persona'),
    path('alumno/', views.alumno.as_view(), name='alumno'),
]
