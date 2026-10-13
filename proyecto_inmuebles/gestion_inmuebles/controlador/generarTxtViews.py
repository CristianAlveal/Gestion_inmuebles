from django.http import HttpResponse
from gestion_inmuebles.models.inmueble import Inmueble


def generar_archivo_txt(inmuebles, titulo):

    contenido = ""
    contenido += titulo.upper() + "\n"
    contenido += "=" * 70 + "\n\n"

    for inmueble in inmuebles:

       # contenido += f"ID: {inmueble.id}\n"
        contenido += f"Nombre: {inmueble.nombre}\n"
        contenido += f"Descripción: {inmueble.descripcion}\n"
       # contenido += f"M² construidos: {inmueble.m2_construidos}\n"
       # contenido += f"M² totales: {inmueble.m2_totales}\n"
       # contenido += f"Habitaciones: {inmueble.habitaciones}\n"
       # contenido += f"Baños: {inmueble.banos}\n"
       # contenido += f"Estacionamientos: {inmueble.estacionamientos}\n"
       # contenido += f"Dirección: {inmueble.direccion}\n"
       # contenido += f"Comuna: {inmueble.comuna}\n"
       # contenido += f"Tipo de inmueble: {inmueble.tipo_inmueble}\n"
       # contenido += f"Precio mensual: ${inmueble.precio_mensual:,.0f}\n"
       # contenido += f"Disponible: {'Sí' if inmueble.disponible else 'No'}\n"

        contenido += "-" * 70 + "\n\n"

    if not inmuebles.exists():
        contenido += "No se encontraron inmuebles.\n"

    response = HttpResponse(
        contenido,
        content_type="text/plain; charset=utf-8"
    )

    response["Content-Disposition"] = (
        'attachment; filename="listado_inmuebles.txt"'
    )

    return response


def generar_listado(request):

    inmuebles = Inmueble.objects.filter(disponible =True)

    return generar_archivo_txt(inmuebles, "Listado de todos los inmuebles")


def generar_listado_comuna(request):

    comuna_id = request.GET.get("comuna")

    inmuebles = Inmueble.objects.filter(
        comuna_id=comuna_id , disponible = True
    )

    return generar_archivo_txt(
        inmuebles,
        "Listado de inmuebles por comuna"
    )


def generar_listado_region(request):

    region_id = request.GET.get("region")

    inmuebles = Inmueble.objects.filter(
        comuna__region_id=region_id, disponible = True
    )

    return generar_archivo_txt(
        inmuebles,
        "Listado de inmuebles por región"
    )
