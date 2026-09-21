from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ia/', views.ia, name='ia'),
    path('linea-tiempo/', views.linea_tiempo, name='linea_tiempo'),
    path('infografias/', views.infografias, name='infografias'),
    path('conceptos/', views.conceptos, name='conceptos'),

]