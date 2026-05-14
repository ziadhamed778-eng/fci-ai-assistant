from fastapi import FastAPI
from pydantic import BaseModel
from generator import StudyGenerator

# تهيئة التطبيق ومحرك الذكاء الاصطناعي
app = FastAPI(title="FCI AI Assistant API")
ai_bot = StudyGenerator()

# تعريف شكل البيانات اللي الباك إند هيبعتها
class ChatRequest(BaseModel):
    message: str

# الـ Endpoint الأساسية
@app.post("/api/chat")
def chat_with_bot(request: ChatRequest):
    """
    هذه هي النقطة (Endpoint) التي سيقوم الباك إند باستدعائها.
    تستقبل سؤال الطالب وترد بالإجابة أو الـ Quiz.
    """
    try:
        reply = ai_bot.chat(request.message)
        return {"status": "success", "response": reply}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# للـ Testing السريع
@app.get("/")
def home():
    return {"message": "AI Engine is running successfully!"}