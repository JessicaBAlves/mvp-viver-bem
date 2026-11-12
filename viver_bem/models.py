from django.db import models
from django.utils import timezone


class Beneficiario(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    composicao_familiar = models.PositiveIntegerField(default=1)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"


class ItemEstoque(models.Model):
    alimento = models.CharField(max_length=100)
    lote = models.CharField(max_length=30)
    data_validade = models.DateField()
    quantidade = models.PositiveIntegerField()
    unidade = models.CharField(max_length=20, default="kg")

    class Meta:
        ordering = ["data_validade"]  # Ordenação automática pelo método FEFO

    @property
    def dias_para_vencer(self):
        return (self.data_validade - timezone.now().date()).days

    def __str__(self):
        return f"{self.alimento} - Lote {self.lote} (Val: {self.data_validade})"


class RegistroEntrega(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    data_entrega = models.DateField(default=timezone.now)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"Entrega: {self.beneficiario.nome} em {self.data_entrega}"
