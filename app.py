import streamlit as st
import requests
import json
from bs4 import BeautifulSoup
from groq import Groq

# 1. Setup the client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# 2. Build the Interface
st.title("AI Website Summarizer")
url = st.text_input("Paste your URL here:")

# 3. Handle the Logic
if st.button("Summarize"):
    if url:
        try:
            st.write("Fetching website...")
            response = requests.get(f"https://api.allorigins.win/get?url={url}", timeout=15)
            
            if response.status_code == 200:
                data = json.loads(response.text)
                soup = BeautifulSoup(data['contents'], 'html.parser')
                text = soup.get_text()[:3000]
                
                st.write("Summarizing...")
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": f"Summarize this: {text}"}],
                    model="llama-3.3-70b-versatile",
                )
                st.write(chat_completion.choices[0].message.content)
            else:
                st.error("Could not fetch the URL.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a URL first.")
