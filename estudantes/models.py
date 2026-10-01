# app - models.py file

from django.db import models

# Create your models here.
class Estudante(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='uploads/', default='foto.png')
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50)
    numero_celular = models.CharField(max_length=15)
    data_de_nascimento = models.DateField()

    def __str__(self):
        return self.nome