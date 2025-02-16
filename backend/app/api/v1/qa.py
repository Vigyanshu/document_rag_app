from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import numpy as np
from app.db.database import get_db, Document, Embedding
import app.services.embeddings as embedding_service
import app.services.llm_services as llm_services

router = APIRouter()

@router.post("/qa/")
def answer_question(question: str, db: Session = Depends(get_db)):
    query_vector = embedding_service.generate_embedding(question)
    
    # Perform FAISS search
    _, indices = embedding_service.index.search(np.array([query_vector]), 5)
    retrieved_indices = [i for i in indices[0] if i != -1]  # Ignore invalid indices
    
    if not retrieved_indices:
        raise HTTPException(status_code=404, detail="No relevant documents found")
    
    # Fetch embeddings efficiently
    embeddings = db.query(Embedding).filter(Embedding.id.in_(retrieved_indices)).all()
    
    # Fetch relevant documents efficiently
    doc_ids = [embedding.document_id for embedding in embeddings]
    relevant_docs = db.query(Document).filter(Document.id.in_(doc_ids)).all()
    
    if not relevant_docs:
        raise HTTPException(status_code=404, detail="No relevant documents found")
    
    # Generate answer using Llama 3.1 8B via vLLM
    answer = llm_services.generate_answer(question, [doc.content for doc in relevant_docs])
    
    return {"question": question, "answer": answer}