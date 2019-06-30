
from django.contrib import admin
from django.urls import path, include

from gg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('rec', views.enviar, name='recuperar'),
    path('pag_rec', views.rec, name='recuva'),
    path('recuperacao/<str:link>', views.recuperacao, name='recebe_recpuperacao'),
]
