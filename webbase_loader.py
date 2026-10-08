from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash", # google/gemma-4-26B-A4B-it  zai-org/GLM-5.2  
    task="text-generation"
) 

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='Answer the following question - \n {question} from the following - \n {text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser()

# url = 'https://www.flipkart.com/apple-macbook-air-m5-2026-m5-16-gb-512-gb-ssd-tahoe-mdhe4hn-a/p/itm8505e2f874525'
# url = 'https://en.wikipedia.org/wiki/India'

url = 'https://docs.langchain.com/'
loader = WebBaseLoader(url)

docs = loader.load()

# print(len(docs))

# print(docs[0].page_content)

chain = prompt | model | parser

print(chain.invoke({'question': 'What are the key highlights that makes langchain different from other', 'text': docs[0].page_content}))
