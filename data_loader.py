from langchain.document_loaders import URLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Extract data from the URL
url = "https://brainlox.com/courses/category/technical"
loader = URLLoader(urls=[url])
documents = loader.load()

# Create embeddings
embeddings = OpenAIEmbeddings()
doc_embeddings = embeddings.embed_documents([doc.page_content for doc in documents])

# Store in a vector store
vector_store = FAISS.from_documents(documents, embeddings)

# Save the vector store to disk
vector_store.save("vector_store.faiss")
