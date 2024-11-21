from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    es_artesano = models.BooleanField(default=False)
    es_comprador = models.BooleanField(default=True)
