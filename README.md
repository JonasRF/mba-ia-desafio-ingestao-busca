# Desafio MBA Engenharia de Software com IA - Full Cycle

- 1- Ingestão: Ler um arquivo PDF e salvar suas informações em um banco de dados PostgreSQL com extensão pgVector.<br>
- 2- Busca: Permitir que o usuário faça perguntas via linha de comando (CLI) e receba respostas baseadas apenas no conteúdo do PDF.

# 🚀 Como Executar a Aplicação

## 📋 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python 3.10+
- Docker e Docker Compose
- Git
- Conta e chave de API do Google Gemini e da OpenAI

---

## 📥 Clonar o repositório

```
git clone https://github.com/JonasRF/mba-ia-desafio-ingestao-busca.git
cd mba-ia-desafio-ingestao-busca
```

# ⚙️ Configurar variáveis de ambiente

Crie um arquivo .env na raiz do projeto com as variáveis necessárias:

```
GOOGLE_API_KEY=your_api_key_here
GOOGLE_EMBEDDING_MODEL='models/embedding-001'
OPENAI_API_KEY=
OPENAI_EMBEDDING_MODEL='text-embedding-3-small'
DATABASE_URL=
PG_VECTOR_COLLECTION_NAME=
PDF_PATH=
```
## ⚠️ Ajuste conforme sua configuração local


# 🐳 Subir infraestrutura (PostgreSQL + pgvector)
```
docker-compose up -d
```

Esse comando irá subir:

--Banco PostgreSQL

--Extensão pgvector para armazenamento de embeddings

🐍 Criar e ativar ambiente virtual
Linux / Mac:
python3 -m venv venv
source venv/bin/activate
Windows:
python -m venv venv
venv\Scripts\activate
📦 Instalar dependências
pip install -r requirements.txt
📄 Executar ingestão de documentos

Caso exista um script de ingestão (ex: ingest.py):

python ingest.py

Esse processo irá:

Ler arquivos PDF

Dividir em chunks

Gerar embeddings

Armazenar no banco vetorial

💬 Executar o sistema de busca (chat)
python main.py

Ou outro arquivo principal do projeto.

Você poderá fazer perguntas como:

Quantas empresas existem no documento?
🧪 Exemplo de uso
Pergunta: Qual é o conteúdo principal do PDF?
Resposta: ...

O sistema responde com base nos dados ingeridos (RAG).
