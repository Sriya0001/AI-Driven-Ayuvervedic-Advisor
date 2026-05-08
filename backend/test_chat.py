from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

try:
    print("Trying ChatGroq")
    chat_model = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant", 
        temperature=0.1
    )
    print(chat_model.invoke("Hello"))
except Exception as e:
    print("Error:", e)
