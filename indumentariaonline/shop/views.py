from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render
from . import forms
from .models import Remera

def index(request):
    remeras = Remera.objects.all()
    ctx = {
        'titulo':'Inicio',
        'headers':["Marca","Talle","Color","Lisa","Género"],
        'remeras':remeras,
    }
    return render(request, "shop/index.html", ctx)

def contacto(request):
    ctx = {
        'titulo':'Contacto'
    }
    return render(request, "shop/contacto.html", ctx)

def nueva_remera(request):
    if request.method == 'POST':
        form = forms.nuevaRemera(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = forms.nuevaRemera()
            
    ctx = {
        'title':'Nueva Remera',
        "form":form
    }
    return render(request, "shop/nueva_remera.html", ctx)