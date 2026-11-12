# mvp-viver-bem
MVP para otimização de distribuição de alimentos - Associação Comunitária Viver Bem
# 🌿 MVP-Viver-Bem — Gestão de Estoque (FEFO) e Entregas Comunitárias

Sistema web desenvolvido em **Python** e **Django** para a **Associação Comunitária Viver Bem**, focado no controle inteligente de doações perecíveis, prevenção de desperdício alimentar e rastreabilidade social de entregas.

---

## 🎯 Funcionalidades Principais

- **Gestão de Inventário FEFO (*First Expired, First Out*):** Ordenação automatizada dos lotes de alimentos por data de validade mais próxima, exibindo alertas visuais de vencimento.
- **Controle de Entregas por CPF:** Registro de distribuição de cestas com validação em tempo real que bloqueia entregas em duplicidade para a mesma família no mesmo mês civil.
- **Acessibilidade (WCAG 2.1):** Barra de acessibilidade integrada com modo de **Alto Contraste** (preto e amarelo), redimensionamento dinâmico de fontes e suporte semântico (`ARIA`) para leitores de tela.
- **Qualidade e CI/CD:** Suíte de testes automatizados com `Pytest` (92% de cobertura) e esteira de Integração Contínua configurada via **GitHub Actions**.

---

## 🛠️ Stack Tecnológica

- **Backend:** Python 3.10, Django 4.2
- **Frontend:** HTML5 Semântico, CSS3 (Modo Alto Contraste), JavaScript
- **Qualidade & Testes:** Pytest, Pytest-Cov, Flake8 (PEP8)
- **DevOps:** GitHub Actions (CI), Render / Railway (Deploy)

---

## 🚀 Como Executar Localmente

```bash
# 1. Clonar o repositório
git clone [https://github.com/JessicaBAlves/mvp-viver-bem.git](https://github.com/JessicaBAlves/mvp-viver-bem.git)
cd mvp-viver-bem

# 2. Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar migrações e iniciar o servidor
python manage.py migrate
python manage.py runserver
