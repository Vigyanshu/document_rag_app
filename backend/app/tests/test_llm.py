import requests
from unittest.mock import patch
import app.services.llm_services as llm_services

@patch("requests.post")
def test_generate_answer(mock_post):
    """Test LLM API response"""
    mock_post.return_value.json.return_value = {"choices": [{"text": "This is a response"}]}
    
    question = "What is AI?"
    context = ["AI is artificial intelligence."]
    answer = llm_services(question, context)
    
    assert "This is a response" in answer