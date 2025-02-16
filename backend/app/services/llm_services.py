import requests
import os

# Load vLLM API URL from environment variables or use default
VLLM_API_URL = os.getenv("VLLM_API_URL", "http://localhost:8000/v1/completions")

def generate_answer(question: str, context: list[str]) -> str:
    """
    Calls the vLLM API to generate an answer based on the retrieved context.
    """
    prompt = f"Context: {' '.join(context)}\nQuestion: {question}\nAnswer:"

    payload = {
        "model": "meta-llama/Llama-3.1-8B",
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.7,
        "top_p": 0.9
    }

    try:
        response = requests.post(VLLM_API_URL, json=payload)
        response.raise_for_status()  # Raise an error if the request fails
        return response.json()["choices"][0]["text"].strip()
    except requests.exceptions.RequestException as e:
        return f"Error communicating with LLM: {str(e)}"