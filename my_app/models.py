from django.db import models

# Create your models here.
class Funcionarios(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
    
    