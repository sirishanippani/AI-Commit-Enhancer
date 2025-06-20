import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

st.title("AI Commit Message Enhancer 🤖")

raw_commit = st.text_area("Enter your raw commit message:")

if st.button("Enhance Commit"):
    if raw_commit.strip() == "":
        st.warning("Please enter a commit message.")
    else:
        prompt = f"""
        You are an expert software engineer. Rewrite the following commit message to make it clear, descriptive, and professional:
        
        Commit: "{raw_commit}"
        
        Enhanced Commit:
        """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a professional software developer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=100
        )

        enhanced_commit = response.choices[0].message.content.strip()

        st.success("Enhanced Commit Message:")
        st.write(enhanced_commit)
