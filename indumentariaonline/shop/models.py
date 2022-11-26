from django.db import models

class Remera(models.Model):
    marca = models.CharField("Marca", max_length=64)
    TALLES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]
    talle = models.CharField("Talle", max_length=3, choices=TALLES)
    color = models.CharField("Color", max_length=64)
    lisa = models.BooleanField("Lisa", blank=True)
    GENERO = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        ('Unisex'   , 'Unisex'),
    ]
    genero = models.CharField("Género", max_length=6, choices=GENERO)