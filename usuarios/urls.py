from django.urls import path
from .views import registro, login_view

app_name = 'usuarios'

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', login_view.as_view(), name='login'),  # Si es una clase, utiliza `.as_view()`
]
