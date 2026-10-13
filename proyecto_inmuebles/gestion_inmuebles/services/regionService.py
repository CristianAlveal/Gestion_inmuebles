from gestion_inmuebles.models.region import Region


class RegionService():

    @staticmethod
    def all_regiones():
        return  Region.objects.all().order_by("nombre")