import os
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()
for k in ("OPENAI_API_KEY", "DATABASE_URL","PG_VECTOR_COLLECTION_NAME"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def search_prompt(question=None):
    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL"))

    store = PGVector(
       embeddings=embeddings,
       collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
       connection=os.getenv("DATABASE_URL"),
       use_jsonb=True,
    )

    # Busca vetorial
    results = store.similarity_search_with_score(question, k=10)
    
    prompt_template = PromptTemplate(
      input_variables=["pergunta", "contexto"],
      template=PROMPT_TEMPLATE
    )
    
    # Monta contexto
    contexto = "\n\n".join([doc.page_content for doc, _ in results])
    
    # Modelo
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
    
    # Chain
    chain = prompt_template | model
    
    # Execução
    response = chain.invoke({"pergunta": question, "contexto": contexto})
    
    return response
  
if __name__ == "__main__":
    search_prompt()  