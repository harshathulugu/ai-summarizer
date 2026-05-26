import streamlit as st
from groq import Groq
from newspaper import Article

# Setup the client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("AI Website Summarizer")
url = st.text_input("Paste your URL here:")

if st.button("Summarize"):
    if url:
        try:
            st.write("Fetching content...")
            # Using newspaper3k to handle the website blocking
            article = Article(url)
            article.download()
            article.parse()
            text = article.text[:3000] # Get the first 3000 chars

            st.write("Summarizing...")
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Summarize this text in 3 bullet points: {text}"}],
                model="llama-3.3-70b-versatile",
            )
            st.write(chat_completion.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid URL.")
