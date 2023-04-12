from django.db import models

class Aplica_compras(models.Model):
    lista = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.id} to {self.lista}'
