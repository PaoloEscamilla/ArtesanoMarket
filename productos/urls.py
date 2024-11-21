from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.catalogo, name='catalogo'),  # Para manejar `/productos/`
    path('<int:id>/', views.detalle_producto, name='detalle'),  # Para manejar `/productos/<id>/`
]
