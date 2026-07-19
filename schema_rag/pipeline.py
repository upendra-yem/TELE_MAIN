from load_schema import file_load
from embed_schema import embed_texts
from store_schema import create_chroma_client
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

chunks = file_load("C:\\Users\\Admin\\Documents\\ML PRO\\Data_Final_Pro\\schema_columns.json")
logger.info("File loading completed. Number of chunks: %d", len(chunks))
embed_texts = embed_texts(chunks)
logger.info("Embedding completed. Number of vectors: %d", len(embed_texts))
collect = create_chroma_client(chunks, embed_texts)
logger.info("Chroma client created and data stored successfully.")