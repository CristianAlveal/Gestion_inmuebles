from django.shortcuts import render, redirect, get_object_or_404
from gestion_inmuebles.models.inmueble import Inmueble
from gestion_inmuebles.services.inmuebleService import InmuebleService
from gestion_inmuebles.services.comunaService import ComunaService
from gestion_inmuebles.services.regionService import RegionService
from gestion_inmuebles.forms.inmuebleForm import Formulario_inmueble
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from gestion_inmuebles.models.usuario import Usuario
from gestion_inmuebles.controlador import usuarioViews
from gestion_inmuebles.models.region import Region
from gestion_inmuebles.models.comuna import Comuna
from gestion_inmuebles.models.solicitud_arriendo import SolicitudArriendo
from django.core.paginator import Paginator
from django.contrib import messages
from django.db import transaction
from django.utils import timezone
# Create your views here.



def entregaContext(request):
    
    context ={'valida_arrendador':usuarioViews.es_arrendador(request.user),
               'valida_arrendatario':usuarioViews.es_arrendatario(request.user),            
               'valida_crear': usuarioViews.puede_crear_inmueble(request.user),
                'es_admin': usuarioViews.es_admin(request.user),
             }
    return context 

# ============================================================ 
# # FUNCIÓN: index  
# # Muestra la página principal con el listado de inmuebles.
# # ============================================================
def index(request):
    
    inmuebles = InmuebleService.all_inmuebles()
      
    # 10 inmuebles por página
    paginator = Paginator(inmuebles, 10)

    # Página solicitada
    numero_pagina = request.GET.get("page")

    pagina_obj = paginator.get_page(numero_pagina)
    
    usuario = getattr(request.user, 'usuario', None)
    
    if request.user.is_authenticated:
            for inmueble in pagina_obj:
                inmueble.tiene_solicitud_usuario = SolicitudArriendo.objects.filter(
                    inmueble=inmueble,
                    arrendatario=request.user
                ).exists()
                
    else:
           for inmueble in pagina_obj:
               inmueble.tiene_solicitud_usuario = False
    
    usuario = getattr(request.user, 'usuario', None)
    
    regiones = RegionService.all_regiones()
    
    comunas = ComunaService.all_comunas()
       
    context = entregaContext(request)
    context.update({             
              'inmuebles': pagina_obj,
              'regiones': regiones,
              'comunas': comunas,
              'usuario': usuario,
              })
    
    return render(request, 'index.html',context)



# ============================================================ 
# # FUNCIÓN: crear_inmueble  
# # Permite crear un nuevo inmueble.
# # ============================================================
@login_required(login_url='index')
@user_passes_test( usuarioViews.puede_crear_inmueble)
def crear_inmueble(request):
    
    inmuebles = request.user.inmuebles.all().order_by('id')
    context = entregaContext(request)
    
    if request.method == "POST":
        form = Formulario_inmueble(request.POST)
      
        resultado, error = InmuebleService.agregar_inmueble(request, form) 
      
        if resultado:
            messages.success(request,'El inmueble fue agregado correctamente.')
              
        else:
             messages.error(request,f'No fue posible agregar el inmueble: {error}')
                
           
        if usuarioViews.es_admin(request.user):
            return redirect('index')
        else:
            return redirect('inmuebles_arrendador')
                
    form = Formulario_inmueble()
    usuario = getattr(request.user, 'usuario', None)
    context.update({                 
                'inmuebles': inmuebles, 
                'puede_crear_inmueble':usuarioViews.puede_crear_inmueble(request.user)  ,
                'form':form,
                'usuario':usuario,                
                })
        
    return render(request, 'agregar_inmueble.html',  context)

    


# ============================================================ 
# # FUNCIÓN:  ver_inmueble_arrendador
# #muestra los inmuebles del artrendador
# # ============================================================
@login_required(login_url='index')
@user_passes_test(usuarioViews.es_arrendador)
def ver_inmueble_arrendador(request):
       
    inmuebles = request.user.inmuebles.all().order_by('id')
    usuario = getattr(request.user, 'usuario', None)
    
    for inmueble in inmuebles:
        inmueble.tiene_solicitudes = inmueble.solicitudes.filter(
        estado='PENDIENTE'
    ).exists()
        
    context = entregaContext(request)       
    context.update({                 
                 'inmuebles': inmuebles, 
                 'puede_crear_inmueble':usuarioViews.puede_crear_inmueble(request.user),
                 'usuario': usuario,                
                 })
    
    return render(request, 'inmuebles_arrendador.html',context)


# ============================================================ 
# # FUNCIÓN:  ver_inmueble_arrendador
# #muestra los inmuebles del artrendador
# # ============================================================
@login_required(login_url='index')
@user_passes_test(usuarioViews.es_arrendatario)
def ver_inmueble_arrendatario(request):
       
    solicitudes = SolicitudArriendo.objects.filter(
        arrendatario=request.user
    ).select_related('inmueble')

    
    usuario = getattr(request.user, 'usuario', None)
    context = entregaContext(request)
    context.update({                
                'solicitudes': solicitudes, 
                'puede_crear_inmueble':usuarioViews.puede_crear_inmueble(request.user)  ,
                'usuario':usuario,
                 })
    
    return render(request, 'inmuebles_arrendatario.html',context)

# ============================================================ 
# # FUNCIÓN: editar_inmueble
# # Permite editar un inmueble existente.
# # ============================================================

@login_required(login_url='index')
@user_passes_test(usuarioViews.puede_editar_inmueble)
def editar_inmueble(request,id):
     
    inmueble = get_object_or_404(Inmueble, pk=id)     
    
    if request.method == "POST":      
          
        resultado, error =  InmuebleService.editar_inmueble(request, id)
              
        if resultado:
            messages.success(request,'El inmueble fue editado correctamente.')
                      
        else:
            messages.error(request,f'No fue posible editar el inmueble: {error}')
       
        if usuarioViews.es_arrendador(request.user):
            return redirect('inmuebles_arrendador')
        else:
            return redirect('index')

    else:
        
        form = Formulario_inmueble(instance=inmueble)
        usuario = getattr(request.user, 'usuario', None)
        context = entregaContext(request)
        context.update({                              
                'puede_crear_inmueble':usuarioViews.puede_crear_inmueble(request.user) ,
                'form':form,
                'usuario':usuario,
                 })
        
        return render(request,'editar_inmueble.html', context )

# ============================================================ 
# # FUNCIÓN: eliminar_inmueble
# # Permite eliminar un inmueble existente.
# # ============================================================
@login_required(login_url='index')
@user_passes_test(usuarioViews.puede_eliminar_inmueble)
def eliminar_inmueble(request,id):
    
    resultado, error =  InmuebleService.eliminar_inmueble(id)
      
    if resultado:
        messages.success(request,'El inmueble fue eliminado correctamente.')
                          
    else:
        messages.error(request,f'No fue posible eliminar el inmueble: {error}')
        
    
    return redirect('index')


@login_required(login_url='index')
@user_passes_test(usuarioViews.es_arrendatario)
def solicitar_arriendo(request, id):
    
    inmueble = get_object_or_404(Inmueble, id=id)
      
      
     # El inmueble debe estar disponible
    if not inmueble.disponible:
        messages.error(
            request,
            'Este inmueble ya no está disponible.'
        )
        return redirect('index') 
    
         # No permitir solicitudes duplicadas pendientes
    if SolicitudArriendo.objects.filter(
        inmueble=inmueble,
        arrendatario=request.user,
        estado='PENDIENTE'
    ).exists():

        messages.warning(
            request,
            'Ya tienes una solicitud pendiente para este inmueble.'
        )

        return redirect('index')

    
    solicitud =SolicitudArriendo.objects.create(
         inmueble=inmueble,
         arrendatario=request.user
        )   
    
    solicitud.save()       
    
    return redirect('index')


@login_required(login_url='index')
@user_passes_test(usuarioViews.es_arrendador)
def gestionar_solicitud(request, idSolicitud):
      
    solicitud = get_object_or_404(
        SolicitudArriendo,
        id=idSolicitud
    )

    # Verificar que el inmueble pertenece al arrendador
    if solicitud.inmueble.usuario != request.user:
        return redirect('index')

    if request.method == 'POST':

        accion = request.POST.get('accion')

        if accion == 'aceptar':
            with transaction.atomic():

                # Aceptar la solicitud seleccionada
                solicitud.estado = 'ACEPTADA'
                solicitud.fecha_respuesta = timezone.now()
                solicitud.save()

                # Rechazar todas las demás solicitudes
                # pendientes del mismo inmueble
                SolicitudArriendo.objects.filter(
                    inmueble=solicitud.inmueble,
                    estado='PENDIENTE'
                ).exclude(
                    id=solicitud.id
                ).update(
                    estado='RECHAZADA'
                )
                
                inmueble = solicitud.inmueble
                
                inmueble.disponible = False
                inmueble.save()

        elif accion == 'rechazar':
            solicitud.estado = 'RECHAZADA'
            solicitud.save()

    return redirect('inmuebles_arrendador')
    