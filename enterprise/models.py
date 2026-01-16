from django.db import models

class Cargos(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
class Setores(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
class TiposDeContrato(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.nome