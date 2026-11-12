from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Beneficiario, ItemEstoque, RegistroEntrega


def dashboard_view(request):
    itens_fefo = ItemEstoque.objects.filter(quantidade__gt=0).order_by("data_validade")
    lotes_criticos = [item for item in itens_fefo if item.dias_para_vencer <= 15]
    context = {
        "itens": itens_fefo,
        "total_lotes_criticos": len(lotes_criticos),
        "total_beneficiarios": Beneficiario.objects.count(),
    }
    return render(request, "dashboard.html", context)


def registrar_entrega_view(request):
    if request.method == "POST":
        cpf = request.POST.get("cpf", "").strip()
        beneficiario = get_object_or_404(Beneficiario, cpf=cpf)
        hoje = timezone.now().date()

        entrega_existente = RegistroEntrega.objects.filter(
            beneficiario=beneficiario,
            data_entrega__year=hoje.year,
            data_entrega__month=hoje.month,
        ).exists()

        if entrega_existente:
            messages.error(
                request,
                f"Bloqueado: {beneficiario.nome} já recebeu cesta neste mês."
            )
            return redirect("registrar_entrega")

        RegistroEntrega.objects.create(beneficiario=beneficiario)
        messages.success(
            request,
            f"Entrega autorizada com sucesso para {beneficiario.nome}."
        )
        return redirect("registrar_entrega")

    return render(request, "registrar_entrega.html")
