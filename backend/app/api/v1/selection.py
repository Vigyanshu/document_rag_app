from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db, Document

router = APIRouter()

@router.get("/documents/")
def list_documents(db: Session = Depends(get_db)):
    """Fetch a list of all available documents."""
    documents = db.query(Document).all()
    return {"documents": [{"id": doc.id, "title": doc.title} for doc in documents]}

@router.post("/documents/select/")
def select_documents(document_ids: list[int], db: Session = Depends(get_db)):
    """Select specific documents to be used in the RAG-based Q&A process."""
    selected_docs = db.query(Document).filter(Document.id.in_(document_ids)).all()
    if not selected_docs:
        raise HTTPException(status_code=404, detail="No valid documents found")
    
    return {"selected_documents": [{"id": doc.id, "title": doc.title} for doc in selected_docs]}