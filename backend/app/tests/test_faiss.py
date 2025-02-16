import numpy as np
from app.services.embeddings import index

def test_faiss_index():
    """Test FAISS index insert and search"""
    vector = np.random.rand(768).astype(np.float32)
    index.add(np.array([vector]))

    _, indices = index.search(np.array([vector]), 1)
    assert indices[0][0] != -1  # Ensure valid index is returned