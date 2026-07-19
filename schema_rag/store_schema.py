import chromadb
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def create_chroma_client(chunks,embed_texts):
    client = chromadb.PersistentClient(path="db")
    logger.info("Chroma client initialized with persistent storage at 'db'.")
    collection = client.get_or_create_collection("schema_collection")
    logger.info("Retrieved or created collection 'schema_collection'.")
    try:
        collection.add(
            ids =[str(i) for i in range(len(embed_texts))],
            documents=chunks,
            metadatas=[{"source": f"chunk_{i}"} for i in range(len(embed_texts))],
            embeddings=embed_texts
        )
        logger.info("Successfully added documents and embeddings to the collection.")   
    except Exception as e:
        logger.error("Error adding documents and embeddings to the collection: %s", str(e))
        raise
    logger.info("Added %d documents and embeddings to the collection.", len(embed_texts))
    logger.info("Vectors stored in the database. Total vectors: %d", len(embed_texts))
    return collection