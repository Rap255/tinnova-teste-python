from django.db import models


class Vehicles(models.Model):
    veiculo = models.CharField(max_length=255,default='')
    marca = models.CharField(max_length=255,default='')
    ano = models.IntegerField(default=1900)
    descricao = models.TextField(max_length=255,default='')
    vendido = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creation date", help_text="Creation date of the user")
    updated = models.DateTimeField(auto_now_add=True)
