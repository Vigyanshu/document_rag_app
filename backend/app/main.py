from fastapi import FastAPI
from app.api.v1.ingestion import router as ingestion_router
from app.api.v1.qa import router as qa_router
from app.db.database import Base, engine
import app.services.embeddings as embedding_service

# Initialize FastAPI App
app = FastAPI(title="Document Management & RAG-based Q&A Application")

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Build FAISS Index at Startup
embedding_service.build_faiss_index()

# Include API Routes
app.include_router(ingestion_router, prefix="/api/v1")
app.include_router(qa_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to the Document Management & RAG-based Q&A Application"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)