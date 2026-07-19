
import os
from dotenv import load_dotenv
from openai import OpenAI
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if os.path.exists(workspace_dir):
    load_dotenv(workspace_dir + "/.env")    
api_key = os.getenv("OPENAI_API_KEY") or os.getenv("API_KEY")
logger.info("Loaded OpenAI API key from environment variables.")
def embed_texts(texts):
    if not texts:
        return []

    client = OpenAI(api_key=api_key)

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )
    vectors = [item.embedding for item in response.data]
    logger.info("Generated embeddings for %d texts.", len(vectors))
    return vectors
