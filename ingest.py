import os
import fitz
import faiss
import numpy as np
import json
import re
from sentence_transformers import SentenceTransformer
from config import DATA_DIR, DB_DIR, EMBEDDING_MODEL

def build_vector_database():
    all_chunks = []
    
    # تأكيد المسارات
    print(f"--- Debug Info ---")
    print(f"Looking for PDFs in: {DATA_DIR}")
    print(f"Database will be saved in: {DB_DIR}")
    
    if not os.path.exists(DATA_DIR):
        print(f"❌ Error: Data directory does not exist!")
        return

    files = [f for f in os.listdir(DATA_DIR) if f.lower().endswith(".pdf")]
    print(f"Found {len(files)} PDF files.")

    for filename in files:
        #if "_Lec" in filename:
            pdf_path = os.path.join(DATA_DIR, filename)
            print(f"📖 Processing: {filename}...")
            # هنا هنادي دالة الاستخراج (تأكد إنها موجودة فوق في ملفك)
            try:
                doc = fitz.open(pdf_path)
                for page_num in range(len(doc)):
                    text = doc.load_page(page_num).get_text("text")
                    clean_text = re.sub(r'\s+', ' ', text).strip()
                    if len(clean_text) > 20:
                        all_chunks.append({
                            "id": f"{filename}_{page_num}",
                            "content": clean_text,
                            "metadata": {"source": filename, "page": page_num + 1}
                        })
            except Exception as e:
                print(f"❌ Error reading {filename}: {e}")

    if not all_chunks:
        print("❌ No text extracted! Check if PDFs are empty or names are wrong.")
        return

    print(f"🚀 Encoding {len(all_chunks)} chunks...")
    model = SentenceTransformer(EMBEDDING_MODEL)
    embeddings = model.encode([c["content"] for c in all_chunks], show_progress_bar=True)

    # حفظ الداتا
    os.makedirs(DB_DIR, exist_ok=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings).astype('float32'))
    
    faiss.write_index(index, os.path.join(DB_DIR, "index.faiss"))
    with open(os.path.join(DB_DIR, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=4)
        
    print(f"✅ Success! Database saved. Files in folder: {os.listdir(DB_DIR)}")

if __name__ == "__main__":
    build_vector_database()