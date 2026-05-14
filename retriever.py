import os
import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from config import DB_DIR, EMBEDDING_MODEL

class StudyRetriever:
    def __init__(self):
        self.index_path = os.path.join(DB_DIR, "index.faiss")
        self.metadata_path = os.path.join(DB_DIR, "metadata.json")
        
        # تحميل الموديل وقاعدة البيانات
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        
        if os.path.exists(self.index_path) and os.path.exists(self.metadata_path):
            self.index = faiss.read_index(self.index_path)
            with open(self.metadata_path, "r", encoding="utf-8") as f:
                self.metadata = json.load(f)
        else:
            raise FileNotFoundError("Database not found! Please run ingest.py first.")

    def retrieve(self, query, k=25): # خليناها 15 عشان يغطي اللائحة كويس
        query_embedding = self.model.encode([query]).astype('float32')
        distances, indices = self.index.search(query_embedding, k)
        
        results = []
        for idx in indices[0]:
            if idx != -1:
                results.append(self.metadata[idx])
        return results