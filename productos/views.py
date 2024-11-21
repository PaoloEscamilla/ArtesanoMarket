from django.shortcuts import render, get_object_or_404
from .models import Producto  # Asegúrate de tener un modelo llamado Producto

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})
def catalogo(request):
    return render(request, 'productos/catalogo.html', {})