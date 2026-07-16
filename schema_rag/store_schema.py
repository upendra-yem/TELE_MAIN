import chromadb

def create_chroma_client(chunks,embed_texts):
    client = chromadb.PersistentClient(path="db")
    collection = client.get_or_create_collection("schema_collection")
    collection.add(
        ids =[str(i) for i in range(len(embed_texts))],
        documents=chunks,
        metadatas=[{"source": f"chunk_{i}"} for i in range(len(embed_texts))],
        embeddings=embed_texts
    )
    print("Vectors stored in the database. Total vectors:", len(embed_texts))
    return collection