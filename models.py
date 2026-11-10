from django.db import models

class Beneficiario(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=150)

class ItemEstoque(models.Model):
    alimento = models.CharField(max_length=100)
    data_validade = models.DateField()
