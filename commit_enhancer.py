import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env (if present)
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def enhance_commit_message(raw_message):
    prompt = f"""
    You are an expert software engineer. Rewrite the following commit message to make it clear, descriptive, and professional:
    
    Commit: "{raw_message}"
    
    Enhanced Commit:
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional software developer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=100
    )
    
    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    raw_commit = input("Enter raw commit message: ")
    enhanced_commit = enhance_commit_message(raw_commit)
    print("\nEnhanced Commit Message:")
    print(enhanced_commit)
