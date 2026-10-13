from gestion_inmuebles.models.comuna import Comuna


class ComunaService():

    @staticmethod
    def all_comunas():
        return  Comuna.objects.all().order_by("nombre")