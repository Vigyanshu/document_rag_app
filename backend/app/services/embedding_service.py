import numpy as np
from langchain.embeddings import EmbeddingModel
from sqlalchemy.orm import Session
from app.models.document import Document, Embedding
import faiss
from app.core.config import settings

index = faiss.IndexFlatL2(settings.EMBEDDING_DIM)

def generate_embedding(content: str) -> np.ndarray:
    embedding_model = EmbeddingModel()
    return np.random.rand(settings.EMBEDDING_DIM).astype(np.float32)  # Replace with actual embedding generation

def store_embedding(db: Session, document_id: int, vector: np.ndarray):
    embedding = Embedding(document_id=document_id, vector=vector.tolist())
    db.add(embedding)
    db.commit()
    index.add(np.array([vector], dtype=np.float32))

def retrieve_similar_documents(query_vector: np.ndarray, db: Session, top_k: int = 5):
    _, indices = index.search(np.array([query_vector]), top_k)
    return [db.query(Document).filter(Document.id == db.query(Embedding).all()[i].document_id).first() for i in indices[0]]