from django.http import JsonResponse
from .models import Autor

def listar_autores(request):
    autor = Autor.objects.all().values('id','nome', 'livros', 'data_cadastro')
    return JsonResponse(list(autor), safe=False)

# Create your views here.
