FoodBot IA

Analisador automático de avaliações com IA — Sentimentos, Resumo e Recomendações

O FoodBot IA é uma aplicação completa que recebe avaliações de clientes e retorna:
Classificação de sentimento (positivo, negativo, neutro), 
Resumo inteligente da avaliação, 
Recomendações de melhoria baseadas em IA, 
Interface web simples e rápida.

O backend foi construído com FastAPI, e o frontend utiliza HTML, CSS e JavaScript para consumir a API.

***Tecnologias Utilizadas***

**Backend**

Python 3.10+, 
FastAPI, 
Pydantic, 
Uvicorn, 
Serviços próprios de ML (sentimento, sumário e recomendações), 
Integração com LLM (caso disponível).

**Frontend**

HTML5, 
CSS3, 
JavaScript (Fetch API).

**Outros**

Docker & Docker Compose (opcional), 
CORS liberado para desenvolvimento.

***Objetivo do Projeto***

O FoodBot IA foi criado para demonstrar:

Backend moderno com FastAPI, 
Integração com modelos de IA, 
Deploy amigável com Docker, 
Comunicação frontend-backend.

Sinta-se à vontade para enviar PRs, sugestões e melhorias!

Como Rodar o Projeto
1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo 
```

2. Criar ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Instalar dependências
```bash
pip install -r requirements.txt
```
4. Rodar o servidor
```bash
uvicorn app.main:app --reload
Servidor iniciará em:
http://localhost:8000
```
5. Acessar o frontend
```bash
Abra no navegador:
http://localhost:8000
```
6. Testar a API (Swagger)
```bash
http://localhost:8000/docs
```








