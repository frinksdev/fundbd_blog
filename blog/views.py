from django.shortcuts import render, get_object_or_404
from .models import post

# Create your views here.
def index(request):
    p=post.objects.order_by("-p_date")
    return render(request,"blog/index.html",{"p":p})

def integrantes(request):
    return render(request,"blog/integrantes.html",{})

def articulo(request,pk):
    p=get_object_or_404(post,pk=pk)
    return render(request,"blog/articulo.html",{"p":p})
