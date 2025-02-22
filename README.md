
# 📚 BookTrack - Gerenciador Inteligente de Leitura

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2%2B-green)](https://www.djangoproject.com)
<div align="center">
  <img src="https://via.placeholder.com/800x400.png?text=BookTrack+Interface" alt="Preview">
</div>

Sistema minimalista para gestão de livros lidos e desejados, desenvolvido em Django com Jinja em 2 horas.

## ✨ Funcionalidades Principais

✅ **CRUD Completo de Livros**  
- Adicione livros com título, autor e status (Lido/Desejado)
- Edite ou exclua registros facilmente
- Prevenção de duplicatas (título + autor)

🔍 **Busca e Filtros Rápidos**  
- Filtre por status de leitura
- Busca instantânea por título/autor

📊 **Dashboard Básico**  
- Contadores de livros lidos vs desejados
- Listagem organizada por data de cadastro

🔐 **Autenticação de Usuários**  
- Sistema completo de login/logout
- Dados isolados por usuário

## 🚀 Como Executar

**Pré-requisitos:**
- Python 3.8+
- Pipenv (ou virtualenv)

**Passos:**
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/booktrack.git
cd booktrack

# Configure ambiente virtual (Pipenv)
pipenv install --dev
pipenv shell

# Execute migrações
python manage.py migrate

# Crie um superusuário (opcional)
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

Acesse no navegador:  
👉 [http://localhost:8000](http://localhost:8000)

## 🛠 Tecnologias Utilizadas

- **Backend:** Django 4.2+
- **Frontend:** Jinja2 + Bootstrap 5
- **Banco de Dados:** SQLite (dev) / PostgreSQL (prod)
- **Deploy Ready:** Configuração pronta para Heroku/PythonAnywhere

## 📌 Próximas Etapas (Roadmap)

- [ ] Sistema de avaliação por estrelas
- [ ] Gráficos interativos de progresso
- [ ] Exportação/importação CSV
- [ ] API REST integrada

## 🤝 Como Contribuir

1. Faça um Fork do projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Add some feature'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

### 📝 Notas Adicionais:
1. Substitua os placeholders ([Seu Nome], links de contato, etc)
2. Adicione screenshots reais no lugar do placeholder
3. Personalize as seções de roadmap conforme sua evolução
4. Para deploy rápido: [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
