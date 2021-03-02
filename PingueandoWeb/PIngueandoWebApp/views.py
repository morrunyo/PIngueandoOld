from django.shortcuts import render
from PIngueandoWebApp import models

# Create your views here.
def pinguers_list(request):
    return render(
        request,
        "PIngueandoWebApp/list.html",
        {
            'datasourceModel': models.Pinguer._meta.get_fields(),   
            'datasource': models.Pinguer.objects.all()



        }
    )