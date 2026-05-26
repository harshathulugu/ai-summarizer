import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("AI Website Summarizer")
url = st.text_input("Paste your URL here:")
if st.button("Summarize"):
    st.write("Processing...")
