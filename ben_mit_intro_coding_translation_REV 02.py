import openai
import os
from dotenv import load_dotenv
import streamlit as st

# Title and Description
st.title("Language Translator")
st.write("Translate English text into other languages using OpenAI's API.")

# Load the API key from the environment variable
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    st.error("API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

openai.api_key = api_key

# Define the translation function
def translate_text(text, target_language):
    prompt = f"Translate the following English text to {target_language}:\n\n{text}"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the latest GPT-3 model
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
    )
    translation = response.choices[0].text.strip()
    return translation

# Streamlit App Interface
text = st.text_area("Enter the English text you want to translate")
target_language = st.selectbox("Select the target language", ["French", "Spanish", "German", "Italian"])

if st.button("Translate"):
    if text:
        with st.spinner('Translating...'):
            translation = translate_text(text, target_language)
        st.success(f"Translated Text ({target_language}):")
        st.write(translation)
    else:
        st.warning("Please enter text to translate.")
