from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    livros = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
   
def __str__(self):
    return self.nome