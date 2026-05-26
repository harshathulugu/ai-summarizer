import streamlit as st
from groq import Groq

# 1. API Key Setup
# Ensure this key is stored in your Streamlit App 'Secrets' menu
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("GROQ_API_KEY is missing in Secrets.")
    st.stop()

st.title("AI Summarizer")

# 2. Text Input
user_input = st.text_area("Paste text to summarize here:", height=200)

# 3. Processing Logic
if st.button("Summarize"):
    if user_input:
        try:
            with st.spinner("Processing..."):
                response = client.chat.completions.create(
                    messages=[{"role": "user", "content": f"Summarize this: {user_input}"}],
                    model="llama-3.3-70b-versatile",
                )
                st.subheader("Summary:")
                st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"AI Error: {e}")
    else:
        st.warning("Please paste some text.")
