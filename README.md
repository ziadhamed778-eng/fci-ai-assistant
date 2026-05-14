🎓 FCI Smart Academic AssistantAn AI-powered RAG system acting as a 24/7 academic advisor and study companion for FCI students.


📌 Project OverviewThe FCI Smart Academic Assistant is an intelligent system designed to bridge the gap between students and complex academic regulations. By leveraging Retrieval-Augmented Generation (RAG), the assistant integrates official faculty bylaws (اللائحة الداخلية) and course materials into a unified vector database to provide accurate, context-aware support.

✨ Key Features

⚖️ Smart Academic Advisor: Acts as a virtual mentor, answering queries regarding credit hour registration, GPA calculation, academic warnings, and specialization requirements based on official regulations.

📖 Intelligent Summarization: Extracts and simplifies core concepts from lecture PDFs, offering different explanation styles (Simple vs. Academic).

📝 Dynamic Quiz Generator: Automatically creates Multiple Choice Questions (MCQs) with varying difficulty levels (Easy, Medium, Hard) to test student knowledge.

⚡ High-Performance REST API: Built with FastAPI, ensuring fast response times and easy integration with Frontend/Mobile applications.

🛠️ Tech StackGenerative AI: Google Gemini 2.0 Flash (LLM for reasoning and generation).RAG Framework: LangChain (Or manual RAG pipeline).Vector Database: FAISS (Facebook AI Similarity Search) for high-speed retrieval.Embeddings: Sentence-Transformers (all-MiniLM-L6-v2) for bilingual semantic mapping.Backend: FastAPI & Uvicorn (Asynchronous API framework).Deployment: Render & GitHub Actions (CI/CD)

.🚀 How It WorksData Ingestion: Faculty bylaws and lectures are processed, chunked, and converted into vector embeddings.Semantic Retrieval: When a student asks a question, the system searches the FAISS index for the most relevant context.Contextual Generation: The retrieved context is fed into the Gemini model with a strict system prompt to prevent hallucinations and ensure responses are strictly based on provided facts.

🔌 API Endpoints (For Developers)EndpointMethodDescription/queryPOSTAsk a question about bylaws or courses./generate-quizPOSTGenerate MCQs based on a specific topic./summarizePOSTGet a summary of a specific lecture.

📦 Installation & SetupClone the repository:Bashgit clone https://github.com/your-username/fci-ai-assistant.git
Install dependencies:Bashpip install -r requirements.txt

Run the server:Bashuvicorn main:app --reload

📝 LicenseThis project is licensed under the MIT License.
