import streamlit as st
from groq import Groq
import requests
from bs4 import BeautifulSoup

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("AI Website Summarizer")

url = st.text_input("Paste your URL here:").strip()

if st.button("Summarize"):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()[:3000]

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": f"Summarize this: {text}"}],
            model="llama-3.3-70b-versatile",
        )
        st.write(chat_completion.choices[0].message.content)
    except Exception as e:
        st.write(f"An error occurred: {e}")
