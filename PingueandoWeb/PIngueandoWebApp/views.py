from django.shortcuts import render
from PIngueandoWebApp import models

# Create your views here.
def pinguers_list(request):
    return render(
        request,
        "PIngueandoWebApp/pinguer_list.html",
        { 
            'datasource': models.Pinguer.objects.all()
        }
    )