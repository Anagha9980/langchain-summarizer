import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

print("1. SCRIPT IS RUNNING (GROQ VERSION)!")

# Look for the .env in the current folder
load_dotenv() 

api_key = os.getenv("GROQ_API_KEY")

if api_key:
    print("2. Success! Groq Key found.")
else:
    print("2. ❌ ERROR: Groq Key not found in .env")

try:
    print("3. Talking to Groq AI...")
    # Using Llama 3 - a powerful free-to-use model on Groq
    llm = ChatGroq(
        model="llama-3.3-70b-versatile", 
        groq_api_key=api_key
    )
    
    res = llm.invoke("Summarize the benefits of using LangChain in one short sentence.")
    print("\n4. --- AI RESPONSE ---")
    print(res.content)
except Exception as e:
    print(f"\n4. ❌ ERROR: {e}")