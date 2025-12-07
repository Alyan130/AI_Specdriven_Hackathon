import os
# Correct import for Qdrant client
from qdrant_client import QdrantClient
import google.generativeai as genai
from dotenv import load_dotenv
from agents import function_tool # Import function_tool for agent integration

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

qdrant_client_instance = QdrantClient(
    url=os.getenv("QDRAUNT_DB_URL"),
    api_key=os.getenv("QDRAUNT_API_KEY")
)

COLLECTION_NAME = "book"
EMBEDDING_MODEL = "gemini-embedding-001"

def get_embedding(text: str) -> list[float]:
    """Generates an embedding for the given text."""
    response = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=text,
        task_type="RETRIEVAL_QUERY"
    )
    return response['embedding']

@function_tool
def retrieve_docs(query: str) -> str:
    """
    Retrieves relevant text chunks from the Qdrant knowledge base based on the query.
    """
    query_embedding = get_embedding(query)

    search_result = qdrant_client_instance.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=3 # Retrieve top 3 relevant chunks
    )

    context = ""
    for hit in search_result:
        context += hit.payload["text"] + "\n\n"

    return context
