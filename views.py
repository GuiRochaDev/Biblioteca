from django.http import JsonResponse
from .models import livro

def listar_livros(request):
    livros = livro.objects.all().values('id','nome', 'data_cadastro')
    return JsonResponse(list(livros), safe=False)
# Create your views here.
