from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='supervision'),
    path('excel/<int:id>', views.excel, name='supervision_excel'),
]