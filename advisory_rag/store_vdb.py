import os

import chromadb

# Get the directory where this script is located (advisory_rag folder)
script_dir = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(script_dir, "db")

print("Database path:", PATH)


def get_chroma_client(vectors, chunks=None):
    client = chromadb.PersistentClient(path=PATH)
    collection = client.get_or_create_collection("advisory_collection")

    if chunks is None:
        documents = [f"chunk_{i}" for i in range(len(vectors))]
    else:
        documents = [chunk.page_content for chunk in chunks]

    collection.add(
        ids=[str(i) for i in range(len(vectors))],
        embeddings=vectors,
        metadatas=[{"source": f"chunk_{i}"} for i in range(len(vectors))],
        documents=documents,
    )
    return collection
