import chromadb
from chromadb.config import Settings

# Initialize Chroma client with default settings
chroma_client = chromadb.Client(Settings())

# Create or retrieve collection
collection = chroma_client.get_or_create_collection("presentation_descriptions")

def add_to_chroma(description, vector):
    collection.add([description], [vector])

def query_chroma(vector, top_k=5):
    results = collection.query(vectors=[vector], top_k=top_k)
    return results
