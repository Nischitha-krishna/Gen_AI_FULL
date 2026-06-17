from src.vector_store import client
from src.embeddings import get_embedding
from config import COLLECTION_NAME

def retrieve_context(query):
    result=client.query_points(
        collection_name=COLLECTION_NAME,
        query=get_embedding(query),
        limit=3
    )
    return "\n\n".join([p.payload["text"] for p in result.points])
