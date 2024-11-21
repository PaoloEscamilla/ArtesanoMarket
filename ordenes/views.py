from django.shortcuts import render

def carrito(request):
    return render(request, 'ordenes/carrito.html', {})

def checkout(request):
    return render(request, 'ordenes/checkout.html', {})