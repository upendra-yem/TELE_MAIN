import json
from langchain_text_splitters import RecursiveCharacterTextSplitter

def file_load(file_path):
    with open(file_path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    if isinstance(data, list):
        records = data
    elif isinstance(data, dict):
        records = [data]
    else:
        records = [str(data)]

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
    return data