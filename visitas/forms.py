# visitas/forms.py
from django import forms
from .models import Visita, Checklist
from datetime import date

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['fecha', 'supervisor', 'zona', 'observaciones', 'estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows':3}),
        }

    def clean_fecha(self):
        f = self.cleaned_data['fecha']
        if f > date.today():
            raise forms.ValidationError("La fecha no puede ser en el futuro.")
        return f


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['item', 'cumplido', 'comentario', 'nivel_riesgo']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows':2}),
        }

    def clean(self):
        cleaned = super().clean()
        cumplido = cleaned.get('cumplido')
        nivel = cleaned.get('nivel_riesgo')
        comentario = cleaned.get('comentario')

        if nivel == 'alto' and not comentario:
            raise forms.ValidationError("Si el nivel de riesgo es Alto, debe agregar un comentario.")
        return cleaned
