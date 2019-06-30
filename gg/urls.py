from django.urls import path, include
from gg import views

urlpatterns = [
    path('send',views.index,name='index'),

]
