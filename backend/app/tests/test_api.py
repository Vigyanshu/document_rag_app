import pytest
from fastapi.testclient import TestClient

def test_ingest_document(client):
    """Test document ingestion"""
    response = client.post("/ingest/", json={"title": "Test Doc", "content": "This is a test document."})
    assert response.status_code == 200
    data = response.json()
    assert "document_id" in data

def test_qa_query(client):
    """Test QA system response"""
    response = client.post("/qa/", json={"question": "What is this document about?"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data