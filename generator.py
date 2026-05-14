from google import genai
from config import GEMINI_API_KEY
from retriever import StudyRetriever

# استخدام المكتبة الجديدة
client = genai.Client(api_key=GEMINI_API_KEY)

class StudyGenerator:
    def __init__(self):
        self.retriever = StudyRetriever()

    def chat(self, user_message):
        # 1. البحث في الداتا بيز
        results = self.retriever.retrieve(user_message, k=15)
        if not results:
            return "عذراً، لم أجد معلومات متعلقة بطلبك في قاعدة البيانات."
            
        context = "\n---\n".join([res['content'] for res in results])
        
        # 2. الـ Prompt الذكي (System Instruction)
        prompt = f"""
        أنت مساعد أكاديمي ومرشد ذكي لطلاب كلية الحاسبات والمعلومات.
        مهمتك تلبية طلب الطالب المكتوب أدناه بناءً على المعلومات المرفقة (Context) فقط.
        
        قواعد الاستجابة:
        - إذا كان الطلب استفساراً عن القوانين (مثل GPA أو التسجيل)، أجب بدقة من اللائحة.
        - إذا طلب الطالب شرحاً، قم بتبسيط المعلومة بطريقة أكاديمية ومنسقة.
        - إذا طلب الطالب أسئلة (Quiz) لاختبار نفسه، قم بتأليف أسئلة اختيارات (MCQ) مع ذكر الإجابة الصحيحة.
        - تحدث باللغة العربية، واحتفظ بالمصطلحات التقنية بالإنجليزية.
        - لا تؤلف أي معلومات من خارج الـ Context.
        
        المعلومات المتاحة (Context):
        {context}
        
        طلب الطالب: "{user_message}"
        """
        
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return response.text
        except Exception as e:
            return f"حدث خطأ في الاتصال بالذكاء الاصطناعي: {e}"