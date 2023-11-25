from django import forms

class MusicoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    instrumento = forms.CharField(required=True, max_length=64)