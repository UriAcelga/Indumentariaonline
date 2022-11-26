from django.forms import ModelForm
from .models import Remera

class nuevaRemera(ModelForm):
    class Meta:
        model = Remera
        fields = ("marca","talle","color","lisa","genero")