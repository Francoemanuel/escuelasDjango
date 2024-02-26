from django.forms import ModelForm
from . models import Escuela

class EscuelaForm(ModelForm):
    class Meta:
        model = Escuela
        exclude = ()