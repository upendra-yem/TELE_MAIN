from openai import OpenAI
import os
from dotenv import load_dotenv

workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if os.path.exists(workspace_dir):
    load_dotenv(workspace_dir + "/.env")
        

api_key = os.getenv("OPENAI_API_KEY") or os.getenv("API_KEY")
if not api_key:
    raise RuntimeError(
        "OpenAI API key is missing. Set OPENAI_API_KEY or API_KEY in the environment or in advisory_rag/.env or .env."
    )

client = OpenAI(
    api_key=api_key
)

def embed_texts(texts):
    if not texts:
        return []

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )
    vectors = [item.embedding for item in response.data]
    return vectors
