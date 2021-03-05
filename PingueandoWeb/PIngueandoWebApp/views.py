from django.shortcuts import render
from django.shortcuts import redirect
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

def pinguers_changeStatus(request,pinguer_id):
    pinguer = models.Pinguer.objects.get(id=pinguer_id)
    pinguer.active = not pinguer.active
    pinguer.save()
    return redirect("/")
