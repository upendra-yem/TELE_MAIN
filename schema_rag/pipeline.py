from load_schema import file_load
from embed_schema import embed_texts
from store_schema import create_chroma_client
chunks = file_load("C:\\Users\\Admin\\Documents\\ML PRO\\Data_Final_Pro\\schema_columns.json")
embed_texts = embed_texts(chunks)
print("Embedding completed. Number of vectors:", len(embed_texts))
collection = create_chroma_client(chunks, embed_texts)