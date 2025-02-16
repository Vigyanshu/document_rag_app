import numpy as np
from app.services.embeddings import generate_embedding

def test_generate_embedding():
    """Test embedding generation"""
    text = "Hello world!"
    vector = generate_embedding(text)
    assert len(vector) == 768
    assert isinstance(vector, np.ndarray)