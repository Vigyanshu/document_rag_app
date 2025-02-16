import numpy as np
import faiss

index = faiss.IndexFlatL2(768)

def generate_embedding(content: str):
    """
    Generate embeddings for the given content.
    Placeholder implementation using random values.
    """
    return np.random.rand(768).astype(np.float32).tolist()

def add_to_faiss_index(vector):
    """
    Add the generated embedding to FAISS index.
    """
    index.add(np.array([vector], dtype=np.float32))