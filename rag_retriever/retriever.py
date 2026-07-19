import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from advisory_rag.store_vdb import collection
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv(ROOT_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY") or os.getenv("API_KEY")
if not api_key:
    raise RuntimeError("OpenAI API key is missing. Set OPENAI_API_KEY or API_KEY in your environment.")

embed_client = OpenAI(api_key=api_key)


def retrieve_chunks(query_text, db_client=None, embed_client=None, k=3):
    if not query_text or not str(query_text).strip():
        raise ValueError("Query text cannot be empty")


    input_vector = embed_client.embeddings.create(
        model="text-embedding-3-small",
        input=str(query_text),
    )
    embedding = input_vector.data[0].embedding
    logger.info("Input vector generated successfully")
    logger.info(f"Input vector dimensions: {len(embedding)}")

    results =  collection.query(
        query_embeddings =[embedding],
        n_results = k
    )
    logger.info(f"Retrieved {len(results['ids'])} chunks from the database")
    return results
