from openai import OpenAI
import os
from dotenv import load_dotenv
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(PATH)
client = OpenAI(
    api_key=os.getenv("API_KEY")
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
