from django.db import models

class Vino(models.Model):
    cosecha = models.SmallIntegerField()
    pais = models.CharField(max_length=30)
    region = models.CharField(max_length=30, null=True)
    designacion = models.CharField(max_length=30, null=True, blank=True)
    puntos = models.SmallIntegerField()
    precio = models.FloatField()
    provincia = models.CharField(max_length=30, null=True)
    nombre = models.CharField(max_length=30)
    cepas = models.CharField(max_length=15)
    bodega = models.CharField(max_length=50)
    stock = models.SmallIntegerField(default=0)
    
    class Meta:
        db_table = "vinoteca"

    def __str__(self):
        texto = "{0} {1}pts"
        return texto.format(self.nombre,str(self.puntos))


"""
Vintage	Country	County	Designation	Points	Price	Province	Title	Variety	Winery
"""