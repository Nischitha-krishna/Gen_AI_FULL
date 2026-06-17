import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
COLLECTION_NAME="hr_policy"
QDRANT_HOST="localhost"
QDRANT_PORT=6333
CHUNK_SIZE=500
CHUNK_OVERLAP=50
