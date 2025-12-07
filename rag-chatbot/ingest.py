import os
# Correct import for Qdrant models
from qdrant_client import QdrantClient, models
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Qdrant client
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

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> list[str]:
    """Chunks text into smaller pieces with optional overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def ingest_content(file_path: str):
    """Reads content, chunks it, generates embeddings, and upserts to Qdrant."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    chunks = chunk_text(content)

    # Prepare points for Qdrant
    points = []
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        points.append(
            models.PointStruct(
                id=i,  # Simple ID, consider more robust ID generation
                vector=embedding,
                payload={"text": chunk, "source": file_path}
            )
        )

    # Create collection if it doesn't exist
    try:
        qdrant_client_instance.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=len(points[0].vector), distance=models.Distance.COSINE)
        )
    except Exception as e:
        print(f"Collection {COLLECTION_NAME} might already exist or error during recreate: {e}")
        pass # For now, just pass if it exists.

    # Upsert points
    qdrant_client_instance.upsert(
        collection_name=COLLECTION_NAME,
        wait=True,
        points=points
    )
    print(f"Ingested {len(points)} chunks into Qdrant collection '{COLLECTION_NAME}'")

if __name__ == "__main__":
    content_file_path = "content.md"  # Assuming content.md is in the project root
    ingest_content(content_file_path)
