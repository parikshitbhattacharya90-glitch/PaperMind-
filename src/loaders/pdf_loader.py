from langchain_unstructured import UnstructuredLoader
from src.splitters.splitter import split_documents


file_paths = [
    r"data\papers\Test_data.pdf"
]


loader = UnstructuredLoader(file_paths)


docs = list(loader.lazy_load())


print(split_documents(docs))
       # only first document

