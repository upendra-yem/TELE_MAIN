import json
from langchain_text_splitters import RecursiveCharacterTextSplitter
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)
logger.info("Starting the file loading process.")
def file_load(file_path):
    with open(file_path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    if isinstance(data, list):
        records = data
        logger.info("Loaded data is a list with %d records.", len(records))

    elif isinstance(data, dict):
        records = [data]
        logger.info("Loaded data is a dictionary with %d keys.", len(data)) 
    else:
        records = [str(data)]
        logger.warning("Loaded data is neither a list nor a dictionary. Treating it as a single string.")

    text_items = []
    for record in records:
        if isinstance(record, (dict, list)):
            text_items.append(json.dumps(record, ensure_ascii=False, sort_keys=True))
        else:
            text_items.append(str(record))

    combined_text = "\n\n".join(text_items)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    data = text_splitter.split_text(combined_text)
    logger.info("Text splitting completed. Number of chunks: %d", len(data))
    return data