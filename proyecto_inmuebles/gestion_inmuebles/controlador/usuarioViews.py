from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from gestion_inmuebles.controlador import usuarioViews
from gestion_inmuebles.models.usuario import Usuario
from gestion_inmuebles.forms.usuarioForm import UsuarioForm
from gestion_inmuebles.forms.agregarUsuarioForm import AgregarUsuarioForm

#fuincion auxiliar para verificar si es admin(is_staf o is_superuser) 
def es_admin(user):
   return user.is_authenticated and user.is_superuser

def es_arrendador(user):
    return user.is_authenticated and user.groups.filter(name='Arrendador').exists()

def es_arrendatario(user):
    return user.is_authenticated and  user.groups.filter(name='Arrendatario').exists()

def puede_crear_inmueble(user):
    return es_admin(user) or es_arrendador(user)

def puede_editar_inmueble(user):
    return es_admin(user) or es_arrendador(user)

def puede_eliminar_inmueble(user):
    return es_admin(user) or es_arrendador(user)



@login_required(login_url='login')
@user_passes_test(es_admin)
def agregar_usuario(request):

    if request.method == 'POST':

        form = AgregarUsuarioForm(request.POST)
      
        if form.is_valid() :

            with transaction.atomic():

                # Crear User de Django
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['nombres'],
                    last_name=form.cleaned_data['apellidos']
                )

                # Crear Usuario
                usuario = form.save(commit=False)
                usuario.usuario = user
                usuario.save()

                # Obtener el grupo seleccionado
                nombre_grupo = usuario.tipo_ususario

                grupo = Group.objects.get(
                    name=nombre_grupo
                )

                # Asignar usuario al grupo
                user.groups.add(grupo)

            return redirect('index')

    else:
        form = AgregarUsuarioForm()

    return render(
        request,
        'agregar_usuario.html',
        {'form': form}
    )
    
    
@login_required
def detalle_usuario(request, id):

    usuario = get_object_or_404(Usuario,id=id)
  
    form = UsuarioForm(instance=usuario)
   
    context ={ 
                 'valida_arrendador':usuarioViews.es_arrendador(request.user),
                  'valida_arrendatario':usuarioViews.es_arrendatario(request.user),            
                  'valida_crear': usuarioViews.puede_crear_inmueble(request.user),
                  'es_admin': usuarioViews.es_admin(request.user),                  
                  'usuario': usuario,
                  'form':form,                 
                  }

    return render(
        request,
        "detalle_usuario.html",
        context
    )
    
    
@login_required
def editar_usuario(request):

    usuario = request.user.usuario
 
    if request.method == "POST":

        form_usuario = UsuarioForm(
            request.POST,
            instance=usuario
        )
        

        if form_usuario.is_valid():

            form_usuario.save()
           

            return redirect("detalle_usuario", usuario.id)


    return redirect("detalle_usuario", usuario.id)