# AI-Driven Ayurvedic Advisor 🌿

An innovative, conversational AI health assistant that merges ancient Ayurvedic wisdom with state-of-the-art Large Language Models (LLMs). This project utilizes **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware advice based on classical Ayurvedic texts.

## 🚀 Features
- **LLaMA 3.1 Powered:** Utilizing the high-performance Llama-3.1-8b model via the Groq API for near-instant responses.
- **RAG Integration:** The chatbot "reads" from a curated library of Ayurvedic PDFs before answering, ensuring high fidelity to traditional knowledge.
- **Context-Aware Memory:** Intelligent conversation history management that maintains context without hitting API token limits.
- **Extensive Knowledge Base:** Built-in support for the *Ayurvedic Pharmacopoeia of India*, *Charaka Samhita*, and works by Dr. Vasant Lad.

## 🛠️ Tech Stack
- **Language Model:** LLaMA 3.1 (via Groq Cloud)
- **Framework:** LangChain
- **Vector Database:** FAISS
- **UI:** Chainlit
- **Embeddings:** HuggingFace Sentence-Transformers (Local)

## 📦 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Sriya0001/AI-Driven-Ayuvervedic-Advisor.git
cd AI-Driven-Ayuvervedic-Advisor
```

### 2. Backend Configuration
Navigate to the backend directory and install the required Python packages:
```bash
cd backend
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the `backend/` directory and add your Groq API key:
```env
GROQ_API_KEY="your_free_groq_api_key_here"
```
*(You can get a free API key at [console.groq.com](https://console.groq.com))*

### 4. Run the Application
Start the Chainlit server:
```bash
chainlit run app.py -w
```
The application will be available at `http://localhost:8000`.

## 📚 Data Source
The advisor is grounded in the following classical and modern texts:
- **Ayurvedic Pharmacopoeia of India (Vols 1-7)**
- **Charaka Samhita** by Acharya Charaka
- **Ayurveda: The Science of Self-Healing** by Dr. Vasant Lad
- **The Yoga of Herbs** by Dr. David Frawley & Dr. Vasant Lad

## 🤝 Results & Performance
During development, we optimized the RAG pipeline to achieve high faithfulness and relevancy scores. By transitioning to **LLaMA 3.1**, we significantly improved inference speed and reasoning capabilities compared to legacy Mistral or GPT-3.5 implementations.

---
Developed as an advanced AI solution for holistic health management.
