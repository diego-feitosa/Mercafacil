from django.db import models

class Contact(models.Model):
    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=13)
