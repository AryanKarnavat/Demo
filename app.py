
import streamlit as st
import openai

st.set_page_config(page_title="T&C ChatMate", layout="centered")

st.title("📜 T&C ChatMate – Ask Your Terms")

openai.api_key = st.secrets["OPENAI_API_KEY"]

tnc_text = st.text_area("Paste the Terms & Conditions:", height=300)
question = st.text_input("Ask your question about the T&C:")

if st.button("Ask") and tnc_text and question:
    with st.spinner("Reading the fine print..."):
        prompt = f"""You are a privacy assistant. The following Terms & Conditions were submitted:

{tnc_text}

When the user asks questions, answer using only this text. Don’t assume anything.
Q: {question}
A:"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            st.success(response.choices[0].message.content.strip())
        except Exception as e:
            st.error(f"Error: {e}")
