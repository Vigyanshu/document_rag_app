from app.db.database import Document, Embedding

def test_create_document(db):
    """Test inserting a document into DB"""
    doc = Document(title="Sample", content="Hello world!")
    db.add(doc)
    db.commit()
    assert doc.id is not None

def test_create_embedding(db):
    """Test inserting an embedding into DB"""
    doc = Document(title="Sample", content="Hello world!")
    db.add(doc)
    db.commit()

    embedding = Embedding(document_id=doc.id, vector=[0.1] * 768)
    db.add(embedding)
    db.commit()

    assert embedding.id is not None