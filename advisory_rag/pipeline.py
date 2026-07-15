from load_pdf import run_pdf
from embed_pdf import embed_texts
from store_vdb import get_chroma_client

chunks = run_pdf()
print("PDF loaded and split into chunks. Total chunks:", len(chunks))

texts = [chunk.page_content for chunk in chunks]
vectors = embed_texts(texts)
print("Embedding completed. Number of vectors:", len(vectors))

try:
    collection = get_chroma_client(vectors)
    print("Vectors stored in the database. Total vectors:", len(vectors))
except Exception as e:
    print(f"Error storing vectors: {e}")
    import traceback
    traceback.print_exc()