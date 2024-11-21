from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('productos/', include('productos.urls')),
    path('ordenes/', include('ordenes.urls')),
    path('', lambda request: HttpResponse("Bienvenido a Artesanos Market"), name='home'),  # Página principal
]
