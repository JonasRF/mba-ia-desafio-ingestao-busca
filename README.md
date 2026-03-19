# Desafio MBA Engenharia de Software com IA - Full Cycle

- 1- Ingestão: Ler um arquivo PDF e salvar suas informações em um banco de dados PostgreSQL com extensão pgVector.<br>
- 2- Busca: Permitir que o usuário faça perguntas via linha de comando (CLI) e receba respostas baseadas apenas no conteúdo do PDF.

# 🚀 Como Executar a Aplicação

## 📋 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python 3.12+
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
OPENAI_API_KEY=sua_chave_aqui
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
GOOGLE_API_KEY=sua_chave_aqui
GOOGLE_EMBEDDING_MODEL=models/embedding-001
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/rag
PG_VECTOR_COLLECTION_NAME=gpt5_collection
PDF_PATH=document.pdf
```
## ⚠️ Ajuste conforme sua configuração local


# 🐳 Subir infraestrutura (PostgreSQL + pgvector)
```
docker-compose up -d
```

Esse comando irá subir:

- Banco PostgreSQL

- Extensão pgvector para armazenamento de embeddings

# 🐍 Criar e ativar ambiente virtual

### Linux / Mac:
```
python3 -m venv venv
source venv/bin/activate
```
## Windows:
```
python -m venv venv
venv\Scripts\activate
```

# 📦 Instalar dependências

```
pip install -r requirements.txt
```

## 📄 Executar ingestão de documentos

Executar o script de ingestão (ex: ingest.py):

```
python src/ingest.py
```

### Esse processo irá:

- Ler arquivos PDF

- Dividir em chunks

- Gerar embeddings

- Armazenar no banco vetorial

💬 Executar o sistema de busca (chat.py)
```
python src/chat.py
```
Você poderá fazer perguntas como:

🧪 Exemplo de uso
```
Faça sua pergunta: Qual o faturamento da Empresa SuperTechIABrazil?
Resposta: O faturamento da Empresa SuperTechIABrazil é R$ 10.000.000,00.

Faça sua pergunta: Quantos clientes temos em 2024?
Resposta: Não tenho informações necessárias para responder sua pergunta.
```

## O sistema responde com base nos dados ingeridos (RAG).

---

# 📊 Arquitetura da Solução

A aplicação segue o padrão **RAG (Retrieval-Augmented Generation)**, combinando um banco vetorial com modelos de linguagem para responder perguntas com base em documentos.

## 🔷 Diagrama de Arquitetura

```mermaid
flowchart TD
    A[Usuário] --> B[Interface CLI - chat.py]
    B --> C[Camada de Busca - search.py]
    C --> D[Pipeline RAG]
    D --> E[Gerador de Embeddings]
    E --> F[Banco Vetorial - PostgreSQL + pgvector]
    F --> G[Busca Semântica]
    G --> H[Contexto Relevante]
    H --> I[LLM - Gemini / LangChain]
    I --> J[Resposta Gerada]
    J --> A

    subgraph Ingestão(ingest.py)
        K[Documentos PDF] --> L[Leitura e Chunking]
        L --> M[Embeddings]
        M --> F
    end
```
#📚 Explicação Técnica
###🔹 LangChain

O projeto utiliza o LangChain como orquestrador do fluxo de IA, permitindo:

- Integração com modelos LLM (ex: OpenAI)

- Criação de pipelines de processamento

- Encadeamento de etapas (chains)

- Abstração de chamadas para embeddings e busca

###🔹 Embeddings

### Embeddings são representações vetoriais de texto que capturam seu significado semântico.

Como são usados no projeto:

- Os documentos PDF são convertidos em texto

- O texto é dividido em pequenos trechos (chunks)

- Cada chunk é transformado em um vetor numérico (embedding)

- Os vetores são armazenados no banco de dados vetorial

#🔹 Banco Vetorial (pgvector)

O projeto utiliza:

- PostgreSQL + extensão pgvector

### Funções principais:

- Armazenar embeddings

- Realizar busca por similaridade

- Recuperar os trechos mais relevantes com base na pergunta

#🔹 Pipeline de Consulta

Quando o usuário faz uma pergunta:

- A pergunta é convertida em embedding

- O sistema busca os vetores mais próximos no banco

- Os trechos mais relevantes são recuperados

- Esses trechos são enviados como contexto para o LLM

- O modelo gera uma resposta baseada nesse contexto
