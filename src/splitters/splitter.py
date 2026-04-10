# src/splitters/text_splitter.py

from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(docs:list):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    result = splitter.split_documents(docs)
    return result