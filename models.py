from django.db import models

from usuarios.models import Usuario
from Autor.models import Autor

class livro(models.Model):
    nome = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


def __str__(self):
    return self.nome