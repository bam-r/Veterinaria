from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('api/citas/', views.obtener_citas, name='obtener_citas'),
    path('api/mascotas/', views.obtener_mascotas, name='obtener_mascotas'),
    path('mascotas/agregar/', views.mascotas_agregar, name='mascotas_agregar'),
    path('citas/agregar/',views.citas_agregar, name='citas_agregar'),
 ]
