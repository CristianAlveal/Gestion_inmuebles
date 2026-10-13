from django.db import transaction
from django.shortcuts import get_object_or_404
from gestion_inmuebles.models.inmueble import Inmueble
from gestion_inmuebles.forms.inmuebleForm import Formulario_inmueble

class InmuebleService():

    @staticmethod
    def all_inmuebles():
        return  Inmueble.objects.all().order_by("id")
        
        
    @staticmethod
    @transaction.atomic
    def agregar_inmueble(request, form):
              
      #  form = Formulario_inmueble(request.POST)        
        try:
            inmueble = form.save(commit=False)

                # Asignamos el usuario que está conectado
            inmueble.usuario = request.user

            inmueble.save()
            
            return True, None
        
        except Exception as e:
        
            return False, str(e)
        
        
    @staticmethod
    @transaction.atomic
    def editar_inmueble(request, id):
  
        try:      
            inmueble = get_object_or_404(Inmueble, pk=id)        
            form = Formulario_inmueble(request.POST, instance=inmueble)
            inmueble = form.save(commit=False)            
            inmueble.save()
            return True, None
                
        except Exception as e:                
            return  False, str(e)
                
            
    
    @staticmethod
    def eliminar_inmueble(id):
        try:  
            inmueble = get_object_or_404(Inmueble, pk=id)
            inmueble.delete() 
            return True, None
            
        except Exception as e:                
            return  False, str(e)
    