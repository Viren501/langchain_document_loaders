from langchain_community.document_loaders import PyPDFLoader
# pip install pypdf
loader = PyPDFLoader("langchain_introduction.pdf")

docs = loader.load()

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)
