from django import forms
from Aplicaciones.Gestion.models import Queja

class FormularioQueja(forms.ModelForm):
    class Meta:
        model = Queja
        fields = '__all__'
        widgets = {'fecha': forms.DateInput(attrs={'type':'date'})}
