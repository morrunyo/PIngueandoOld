"""
PingueandoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path
from PIngueandoWebApp.scaffolding import PinguerCrudManager
from PIngueandoWebApp.scaffolding import PinguerEventCrudManager

pinguer_crud = PinguerCrudManager()
pinguerevent_crud = PinguerEventCrudManager()

urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls),
    #path('', pinguer_crud.get_list_class_view().as_view)
]

urlpatterns += pinguer_crud.get_url_patterns()
urlpatterns += pinguerevent_crud.get_url_patterns()
