#Custom Chatbot Using Langchain
This project creates a custom chatbot that extracts data from a specific URL, generates embeddings, and handles conversations through a Flask RESTful API.

Getting Started
Prerequisites
Python 3.x
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Setup
Extract Data & Create Embeddings:

Run data_loader.py to load data from the URL, generate embeddings, and store them in a vector store.
Start the API:

Run main.py to start the Flask server.
Usage
Send a POST request to http://localhost:5000/chat with a JSON body:
json
Copy code
{
  "message": "Your question here"
}
The chatbot will respond with the most relevant information based on the data it has processed.
