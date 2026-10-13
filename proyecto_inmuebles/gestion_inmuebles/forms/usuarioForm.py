from django import forms
from django.contrib.auth.models import User
from gestion_inmuebles.models.usuario import Usuario


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
            'nombres',
            'apellidos',
            'telefono',
            'direccion',            
        ]

        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',           
        }

        widgets = {
            'nombres': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'apellidos': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            
        }