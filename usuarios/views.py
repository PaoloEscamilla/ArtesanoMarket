from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

# Vista para el registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autentica automáticamente al usuario registrado
            return redirect('productos:catalogo')  # Cambia la ruta si es necesario
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

# Vista para el login (usando Django's LoginView)
class login_view(LoginView):
    template_name = 'usuarios/login.html'
