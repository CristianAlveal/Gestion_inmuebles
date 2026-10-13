from django import forms
from django.contrib.auth.models import User
from gestion_inmuebles.models.usuario import Usuario


class AgregarUsuarioForm(forms.ModelForm):

    username = forms.CharField(
        label='Nombre de usuario',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nombre de usuario'
        })
    )

    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese contraseña'
        })
    )

    email = forms.EmailField(
        label='Correo electrónico',
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        })
    )

    class Meta:
        model = Usuario
        fields = [
            'nombres',
            'apellidos',
            'telefono',
            'direccion',
            'tipo_ususario'
        ]

        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'tipo_ususario': 'Tipo de usuario',
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
            'tipo_ususario': forms.Select(attrs={
                'class': 'form-select'
            }),
        }