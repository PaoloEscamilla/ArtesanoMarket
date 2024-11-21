from django.urls import path
from . import views

app_name = 'ordenes'

urlpatterns = [
    path('carrito/', views.carrito, name='carrito'),          # Ver carrito
    path('checkout/', views.checkout, name='checkout'),      # Proceso de compra
    path('carrito/', views.carrito, name='carrito'),
]
