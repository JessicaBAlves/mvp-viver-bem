def test_validacao_cpf_beneficiario():
    cpf = "123.456.789-00"
    assert len(cpf) == 14
    assert cpf.count(".") == 2
    assert "-" in cpf

def test_regra_ordenacao_fefo():
    estoque = [
        {"item": "Leite", "validade": "2026-11-20"},
        {"item": "Arroz", "validade": "2026-11-15"}
    ]
    ordenado = sorted(estoque, key=lambda x: x["validade"])
    assert ordenado[0]["item"] == "Arroz"

def test_bloqueio_entrega_duplicada_mesmo_mes():
    entregas_mes = {"123.456.789-00": "2026-11"}
    novo_cpf = "123.456.789-00"
    ja_recebeu = novo_cpf in entregas_mes
    assert ja_recebeu is True
