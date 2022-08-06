from django.shortcuts import render

# Create your views here.
from .models import Director, Pelicula

def index(request):
    num_peliculas = Peliculas.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_peliculas': num_peliculas
        }
    )
