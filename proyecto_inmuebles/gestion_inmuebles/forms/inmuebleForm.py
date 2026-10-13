from django import forms
from gestion_inmuebles.models.inmueble import Inmueble
from django.core.validators import MinValueValidator
from gestion_inmuebles.models.region import Region
from gestion_inmuebles.models.comuna import Comuna


class Formulario_inmueble(forms.ModelForm):

    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        required=True,
        empty_label="Seleccione una región",
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'id_region'
            }
        )
    )

    class Meta:

        model = Inmueble

        fields = [
            'nombre',
            'descripcion',
            'm2_construidos',
            'm2_totales',
            'estacionamientos',
            'habitaciones',
            'banos',
            'direccion',
            'region',
            'comuna',
            'tipo_inmueble',
            'precio_mensual'
        ]

  
    
        widgets = {

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: Casa familiar'
                }
            ),

            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'cols':30,                     
                    'placeholder': 'Descripción del inmueble'
                }
            ),

            'm2_construidos': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'm² construidos',
                     'min': 0
                }
            ),

            'm2_totales': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'm² totales',
                     'min': 0
                }
            ),

            'estacionamientos': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                     'min': 0
                }
            ),

            'habitaciones': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                     'min': 0
                }
            ),

            'banos': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                     'min': 0
                }
            ),

            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: Av. Providencia 1234'
                }
            ),

            'comuna': forms.Select(
                attrs={
                    'class': 'form-select',
                    'id': 'id_comuna'
                }
            ),
            
            'tipo_inmueble': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'precio_mensual': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio mensual',
                     'min': 0
                }
            ),
        }
    
        m2_construidos = forms.FloatField(
                validators=[MinValueValidator(0, message ='El valor no puede ser negativo.')]
            )
        
        m2_totales = forms.FloatField(
            validators=[MinValueValidator(0, message ='El valor no puede ser negativo.')]
            )
        
        estacionamientos = forms.IntegerField(
            validators=[MinValueValidator(0, message ='El valor no puede ser negativo.')]
            )
        
        habitaciones = forms.IntegerField(
                validators=[MinValueValidator(0, message ='El valor no puede ser negativo.')]
            )
        
        banos = forms.IntegerField(
            validators=[MinValueValidator(0, message ='El valor no puede ser negativo.')]
            )
        
        precio_mensual = forms.DecimalField(
                validators=[MinValueValidator(0, message ='El valor no puede ser negativo.')]
            )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Inicialmente no mostramos comunas
        self.fields['comuna'].queryset = Comuna.objects.none()

        # Si estamos editando un inmueble existente
        if self.instance and self.instance.pk:

            comuna = self.instance.comuna

            if comuna:
                self.fields['region'].initial = comuna.region

                self.fields['comuna'].queryset = Comuna.objects.filter(
                    region=comuna.region
                )

        # Si el usuario ya seleccionó una región
        if 'region' in self.data:

            try:
                region_id = int(self.data.get('region'))

                self.fields['comuna'].queryset = Comuna.objects.filter(
                    region_id=region_id
                )

            except (ValueError, TypeError):
                self.fields['comuna'].queryset = Comuna.objects.none()
