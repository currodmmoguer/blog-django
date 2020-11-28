from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404 
from . import utils

# Create your views here.


def index(request):
    
    try:
        id_descripcion = int(Info.objects.filter(key="entrada_descripcion").get().value)
        entrada_descripcion = Post.objects.get(pk=id_descripcion)
    except Info.DoesNotExist:
        entrada_descripcion = None
    
    context = {
        'posts': Post.objects.filter(published_date__lte=timezone.now()).exclude(pk=id_descripcion).order_by('-published_date'),
        'descripcion': entrada_descripcion,
    }
    
    return render(request, 'index.html', context)

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    utils.add_visit(post)
    return render(request, 'post.html', {'post': post})