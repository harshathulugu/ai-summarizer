import streamlit as st
from groq import Groq
import requests
from bs4 import BeautifulSoup

# Use the secure secret key
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("AI Website Summarizer")
url = st.text_input("Paste your URL here:")

if st.button("Summarize"):
    if url:
        try:
            st.write("Fetching website...")
            headers = {"User-Agent": "Mozilla/5.0"}
            # The timeout=10 here stops it from freezing
           response = requests.get(f"https://api.allorigins.win/get?url={url}", timeout=15)
            
            if response.status_code == 200:
    import json
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
                st.error(f"Failed to load website. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a URL first.")
