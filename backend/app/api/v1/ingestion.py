from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import numpy as np
from app.db.database import get_db, Document, Embedding
import app.services.embeddings as embedding_service

router = APIRouter()

@router.post("/ingest/")
def ingest_document(title: str, content: str, db: Session = Depends(get_db)):
    document = Document(title=title, content=content)
    db.add(document)
    db.commit()
    db.refresh(document)
    
    vector = embedding_service.generate_embedding(content)
    embedding = Embedding(document_id=document.id, vector=vector)
    db.add(embedding)
    db.commit()
    
    embedding_service.add_to_faiss_index(vector)
    
    return {"message": "Document ingested successfully", "document_id": document.id}