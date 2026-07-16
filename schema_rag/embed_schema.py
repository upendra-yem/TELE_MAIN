
import os
from dotenv import load_dotenv
from openai import OpenAI

workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if os.path.exists(workspace_dir):
    load_dotenv(workspace_dir + "/.env")    
api_key = os.getenv("OPENAI_API_KEY") or os.getenv("API_KEY")
def embed_texts(texts):
    if not texts:
        return []

    client = OpenAI(api_key=api_key)

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )
    vectors = [item.embedding for item in response.data]
    return vectors
