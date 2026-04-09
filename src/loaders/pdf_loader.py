from langchain_unstructured import UnstructuredLoader

file_paths = [
    r"data\papers\Test_Research_Paper.pdf"
]


loader = UnstructuredLoader(file_paths)


docs = loader.lazy_load()

for doc in docs:
    print(doc)
       # only first document
