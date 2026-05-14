import os

# إعداد المسارات الديناميكية
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_DIR = os.path.join(BASE_DIR, "database")

# التأكد من إنشاء الفولدرات
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True)

# إعدادات الموديلز
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'
# حط مفتاح الـ API بتاعك هنا
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"