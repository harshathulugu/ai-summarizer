try:
            st.write("Fetching website...")
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
                st.error("Could not fetch the URL.")
        except Exception as e:
            st.error(f"Error: {e}")
