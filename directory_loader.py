from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='/books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))

# 1st page of 1st book
print(docs[0].page_content)
print(docs[0].metadata)

# Last page(392-1=391) of 1st book
print(docs[391].page_content)
print(docs[391].metadata)
