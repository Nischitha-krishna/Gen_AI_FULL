from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from config import COLLECTION_NAME,QDRANT_HOST,QDRANT_PORT
from src.embeddings import get_embedding

client=QdrantClient(host=QDRANT_HOST,port=QDRANT_PORT)

def create_collection():
    try:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=1536,distance=Distance.COSINE)
        )
    except Exception:
        pass

def store_chunks(chunks):
    points=[]
    for idx,chunk in enumerate(chunks):
        points.append({
            "id":idx,
            "vector":get_embedding(chunk.page_content),
            "payload":{"text":chunk.page_content}
        })
    client.upsert(collection_name=COLLECTION_NAME,points=points)
