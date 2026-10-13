from django.urls import path
from gestion_inmuebles.controlador import inmuebleViews, views, usuarioViews, generarTxtViews





urlpatterns = [
    path('', inmuebleViews.index, name='index'),
    path('acerca/', views.acerca, name='acerca'),
    path( 'crear_inmueble/', inmuebleViews.crear_inmueble, name='crear_inmueble' ),   
    path( 'editar_inmueble/<int:id>', inmuebleViews.editar_inmueble, name='editar_inmueble' ), 
    path( 'eliminar_inmueble/<int:id>', inmuebleViews.eliminar_inmueble, name='eliminar_inmueble' ),
    path('comunas/<int:region_id>/', views.obtener_comunas, name='obtener_comunas'),
    path('inmuebles_arrendador/', inmuebleViews.ver_inmueble_arrendador, name='inmuebles_arrendador' ),
    path('inmuebles_arrendatario/', inmuebleViews.ver_inmueble_arrendatario, name='inmuebles_arrendatario' ),
    path('agregar_usuario/',usuarioViews.agregar_usuario, name='agregar_usuario'),
    path("generar_listado/",generarTxtViews.generar_listado,name="generar_listado"),
    path("generar_listado-comuna/",generarTxtViews.generar_listado_comuna,name="generar_listado_comuna"),
    path("generar_listado-region/",generarTxtViews.generar_listado_region,name="generar_listado_region"),
    path("usuario/<int:id>/",usuarioViews.detalle_usuario, name="detalle_usuario"),
    path("editar_usuario/",usuarioViews.editar_usuario, name="editar_usuario"),
    path("solicitar_arriendo/<int:id>", inmuebleViews.solicitar_arriendo,name="solicitar_arriendo"),
    path("gestionar_solicitud/<int:idSolicitud>", inmuebleViews.gestionar_solicitud,name="gestionar_solicitud"),

]