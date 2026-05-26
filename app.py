import streamlit as st
from groq import Groq

# Setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("AI Summarizer")
user_input = st.text_area("Paste text to summarize here:")

if st.button("Summarize"):
    if user_input:
        try:
            st.write("Summarizing...")
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Summarize this: {user_input}"}],
                model="llama-3.3-70b-versatile",
            )
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please paste some text.")
