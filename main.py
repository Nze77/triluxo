from flask import Flask, request, jsonify
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain

app = Flask(__name__)

# Load the vector store
vector_store = FAISS.load("vector_store.faiss", OpenAIEmbeddings())

# Create a ConversationalRetrievalChain
conversation_chain = ConversationalRetrievalChain(vector_store)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = conversation_chain.run(input=user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000)
