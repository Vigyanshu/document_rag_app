# Document Management & RAG-based Q&A Application

This application allows users to ingest documents, retrieve relevant documents using FAISS, and generate answers using a language model.

## 📌 Features
- **Document Ingestion**: Store documents and generate embeddings.
- **Retrieval-Augmented Generation (RAG)**: Retrieve relevant documents for queries.
- **LLM Integration**: Answer questions using `meta-llama/Llama-3.1-8B` via `vLLM`.
- **FAISS Indexing**: Fast document retrieval using vector search.
- **PostgreSQL with pgvector**: Store embeddings efficiently.

---

## ⚙️ Setup & Installation

### 1️⃣ **Clone the Repository**
```sh
$ git clone https://github.com/Vigyanshu/document_rag_app.git
$ cd document_rag_app
```

### 2️⃣ **Create a Virtual Environment & Install Dependencies**
```sh
$ python -m venv venv
$ source venv/bin/activate  # On Windows use: venv\Scripts\activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

### 3️⃣ **Setup PostgreSQL Database**
1. Install PostgreSQL and enable `pgvector` extension.
2. Create a new database.
3. Update `DATABASE_URL` in `.env`:
   ```ini
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```
4. Apply migrations:
   ```sh
   $ alembic upgrade head
   ```

### 4️⃣ **Start FAISS Indexing**
```sh
$ python -m app.services.embeddings
```

### 5️⃣ **Start vLLM Server**
```sh
$ vllm serve "meta-llama/Llama-3.1-8B"
```

### 6️⃣ **Run the Application**
```sh
$ uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🚀 Deployment on GitHub Actions & Docker

### 1️⃣ **Build Docker Image**
```sh
$ docker build -t document-rag-app .
```

### 2️⃣ **Run Docker Container**
```sh
$ docker run -p 8000:8000 --env-file .env document-rag-app
```

### 3️⃣ **Setup GitHub Actions (CI/CD)**
1. Create a `.github/workflows/deploy.yml` file:
   ```yaml
   name: Deploy App
   on:
     push:
       branches:
         - main
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout Code
           uses: actions/checkout@v3
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.10'
         - name: Install Dependencies
           run: |
             pip install --upgrade pip
             pip install -r requirements.txt
         - name: Run Tests
           run: pytest
     deploy:
       runs-on: ubuntu-latest
       needs: build
       steps:
         - name: Deploy to Server
           run: |
             ssh user@server "cd /path/to/app && git pull && docker-compose up --build -d"
   ```

2. Add `secrets.GH_DEPLOY_KEY` to GitHub (for SSH deploy access).

---

## 🛠 Testing
Run unit tests:
```sh
$ pytest tests/
```

## 🎯 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/ingest/` | Ingest a document |
| POST   | `/qa/` | Retrieve & answer questions |

---

## 📜 License
MIT License. See `LICENSE` for details.
