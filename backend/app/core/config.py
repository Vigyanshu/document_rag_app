import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
    EMBEDDING_DIM: int = 768
    FAISS_INDEX_PATH: str = "faiss_index.bin"
    API_PREFIX: str = "/api/v1"
    
    class Config:
        env_file = ".env"

settings = Settings()