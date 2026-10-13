from django.shortcuts import render
from django.http import JsonResponse
from gestion_inmuebles.models.comuna import Comuna

def es_admin(user):
   return user.is_authenticated and user.is_superuser


def es_arrendador(user):
    return user.is_authenticated and user.groups.filter(name='Arrendador').exists()


def es_arrendatario(user):
    return user.is_authenticated and user.groups.filter(name='Arrendatario').exists()

def acerca(request):   
    usuario = getattr(request.user, 'usuario', None)
    context ={ 
                 'valida_arrendador':es_arrendador(request.user)  ,
                 'valida_arrendatario':es_arrendatario(request.user),
                 'es_admin': es_admin(request.user),
                 'usuario': usuario,
            }
    return render(request, 'acerca.html',context)

def obtener_comunas(request, region_id):

    comunas = Comuna.objects.filter(
        region_id=region_id
    ).values(
        'id',
        'nombre'
    )

    return JsonResponse(
        list(comunas),
        safe=False
    )